#!/usr/bin/env python3
"""Run the preserved gate checks and the complementary resource/loss checks.

The normal command compares both stable summaries and regenerates the resource
SVG. --json prints the supplemental summary without overwriting either expected
file. --no-figure runs every mathematical check without regenerating the SVG.
"""

import argparse
import json
from pathlib import Path

import check_damped_channel
import check_resources
import check_spectral_frontier
import resource_examples
import verify_bus


def supplemental_checks(regenerate_figure=True):
    resources, first = check_resources.run_checks()
    frontier, second = check_spectral_frontier.run_checks()
    channel, third = check_damped_channel.run_checks()
    examples, fourth = resource_examples.run_checks(regenerate_figure)
    summary = {
        'schema_version': 1, 'status': 'pass',
        **resources,
        'spectral_frontier': frontier,
        'damped_channel': channel,
        'resource_examples': examples,
        'scope': 'Finite construction, convention, and formula checks; analytical proofs remain necessary.',
    }
    return summary, {**first, **second, **third, **fourth}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--json', action='store_true', help='print the supplemental stable summary')
    parser.add_argument('--no-figure', action='store_true', help='check without regenerating the resource SVG')
    args = parser.parse_args()
    baseline, baseline_diagnostics = verify_bus.run_checks()
    expected_baseline = json.loads(Path(__file__).with_name('expected_results.json').read_text(encoding='utf-8'))
    assert baseline == expected_baseline, 'Preserved gate summary differs from expected_results.json.'
    summary, diagnostics = supplemental_checks(not args.no_figure)
    if args.json:
        print(json.dumps(summary, indent=2))
        return
    expected = json.loads(Path(__file__).with_name('expected_supplemental.json').read_text(encoding='utf-8'))
    assert summary == expected, 'Supplemental summary differs from expected_supplemental.json; inspect --json.'
    print('PASS: preserved gate suite and supplemental resource/loss suite.')
    print('Both stable summaries match. General results depend on science/ proofs.')
    for name, value in {**baseline_diagnostics, **diagnostics}.items():
        print(f'{name}: {value:.3e}')


if __name__ == '__main__':
    main()
