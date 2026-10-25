"""Run the finite checks and regenerate the model resource example."""
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = (
    'check_matching.py',
    'check_spectral_frontier.py',
    'check_damped_channel.py',
    'resource_examples.py',
)

if __name__ == '__main__':
    for script in SCRIPTS:
        print(f'Running {script}', flush=True)
        subprocess.run([sys.executable, str(ROOT / 'verification' / script)], cwd=ROOT, check=True)
    print('All finite checks passed. General claims depend on the analytical proofs.')
