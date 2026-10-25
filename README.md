# Quantum Bus Congestion archival snapshot

Source: https://github.com/GoGoKo699/Quantum-Bus-Congestion

Captured 2026-10-25. Original main commit: `9c3cdaa9df4e73c98938736c00887749f0133550`. Original main tree: `afe40f4300a303fdade5f09b5e480b2363100d28`. The source repository was read only throughout acquisition; this package contains no server credentials.

## What is preserved

The self-contained Git bundle preserves all **7 original commits, 3 branches, 1 tag, and 2 pull-request head refs** captured from the source. It contains **77 unique objects: 7 commits, 19 trees, and 51 blobs**. Commit IDs, parent relationships, author and committer identities, timestamps/timezones, messages, file bytes, paths and modes, and original signature bytes are retained exactly. Three commits have signatures. GitHub's recorded signature-verification metadata is retained; no independent OpenPGP trust-chain verification is claimed.

The compressed metadata preserves repository information; both merged PRs including their descriptions, details, changed-file lists, commits, events and timelines; the single release; and explicit empty comment, review, asset and run inventories. There are 0 standalone issues, 0 issue/review/commit comments on reachable commits, 0 reviews/review threads, 0 uploaded release assets, and 0 Actions runs. Four repository issue events and eight PR timeline entries are retained. All seven reachable commits were queried individually for commit comments. GitHub-generated tag ZIP/tar downloads can be regenerated from the preserved tag; they are not separately uploaded release assets.

## File map

| File | Purpose |
|---|---|
| `quantum-bus-congestion.bundle` | Complete original reachable Git history and refs, without prerequisites or network access. |
| `quantum-bus-congestion-metadata.json.gz` | UTF-8 JSON containing source/API records, capture provenance and coverage limits, original Git commit/tree API data and exact-object reconstruction procedures. |
| `verification.json` | Original refs, all object hashes and sizes, signature preservation notes, all current file hashes, public metadata counts and independent restoration results. |
| `MIGRATION.md` | Complete source-to-destination scientific map for all 27 current source files. |
| `SHA256SUMS` | SHA-256 integrity checks for the archive files. |

Retain these files together on the dedicated destination branch `archive/quantum-bus-congestion-history-20261025` in `GoGoKo699/Quantum-Bus-Parallelism`. Original source paths remain unchanged inside the bundle. Git and platform records map through original object IDs, issue/PR numbers and URLs.

The destination also has a separately browsable [exact source snapshot](https://github.com/GoGoKo699/Quantum-Bus-Parallelism/tree/dfee0abb426912063b40347d89123084627cc0ce), at commit `dfee0abb426912063b40347d89123084627cc0ce` on `archive/quantum-bus-congestion-source-20261025`. Its tree is the original source tree `afe40f4300a303fdade5f09b5e480b2363100d28`. That snapshot commit is a destination copy; the bundle preserves the original source commit IDs and full history. The migration's `MIGRATION.md` records the scientific source-to-destination mapping separately.

## Restore and inspect offline

Run these commands in the directory containing the archive files, using a fresh destination path:

```bash
sha256sum -c SHA256SUMS
git -c protocol.allow=never -c protocol.file.allow=always clone --mirror quantum-bus-congestion.bundle Quantum-Bus-Congestion.git
git --git-dir=Quantum-Bus-Congestion.git fsck --full --strict
git --git-dir=Quantum-Bus-Congestion.git bundle verify "$PWD/quantum-bus-congestion.bundle"
git --git-dir=Quantum-Bus-Congestion.git for-each-ref --format='%(refname) %(objectname)'
git --git-dir=Quantum-Bus-Congestion.git log --all --oneline --decorate
gzip -dc quantum-bus-congestion-metadata.json.gz > quantum-bus-congestion-metadata.json
git --git-dir=Quantum-Bus-Congestion.git archive --format=tar refs/heads/main > quantum-bus-congestion-main.tar
```

To create an ordinary working copy from the restored mirror:

```bash
git clone Quantum-Bus-Congestion.git Quantum-Bus-Congestion
```

A mirror restore keeps the two `refs/pull/*/head` refs. An ordinary clone does not normally copy special PR refs; retain the mirror or bundle for the complete archive. GitHub owns `refs/pull/*` on the server. Do not blindly mirror-push the restored repository over an existing destination; any future publication should use a new repository and deliberately choose writable names for PR heads. Metadata JSON preserves source records but cannot recreate GitHub-managed issue/PR IDs, URLs, authorship records or timestamps.

## Original ref map

| Ref | Original object ID |
|---|---|
| `refs/heads/furnishing-haeffner-route` | `951a817eeeec817b5b9837816b27177196ab4f9c` |
| `refs/heads/main` | `9c3cdaa9df4e73c98938736c00887749f0133550` |
| `refs/heads/research/quantum-bus-congestion` | `80928b06d823f4b4f43292c4cda829f6178d4736` |
| `refs/pull/1/head` | `80928b06d823f4b4f43292c4cda829f6178d4736` |
| `refs/pull/2/head` | `951a817eeeec817b5b9837816b27177196ab4f9c` |
| `refs/tags/v1.0.0` | `9c3cdaa9df4e73c98938736c00887749f0133550` |

## Verification performed

Every Git object was checked against its original SHA-1 before being written. The bundle passed `git bundle verify` without prerequisites. A fresh mirror restore with network protocols disabled passed `git fsck --full --strict`. All 6 refs and all 77 object IDs, types, lengths and SHA-256 hashes matched. All 27 files in the original main snapshot were independently recovered and compared byte-for-byte. Source refs were re-read at `2026-10-25T14:51:38.516Z` and still matched. All 34 metadata capture files match the hashes in their capture manifest. The compressed JSON passed decompression and JSON round-trip verification.

## Coverage limits

This is a complete backup of Git objects reachable from the captured refs and the requested available public issue/PR/release/run metadata. It is **not a certified backup of every GitHub service feature**:

- Wiki is enabled in repository settings, but page existence and content were not verified or archived.
- Repository-wide labels, milestones, workflow-definition and artifact inventory endpoints are unsupported by the connected reader. All issue/PR label and milestone assignments are preserved (empty or null); tracked workflow files are covered by Git. Actions reports 0 runs, so no current run logs or artifacts were available to archive.
- The repository-wide commit-comment collection endpoint is unsupported; all 7 reachable commits were queried individually and have no comments. Comments attached only to unreachable or deleted commits are outside coverage.
- Deleted or unadvertised refs, unreachable objects, deleted issue history, expired/deleted Actions data, external link targets, admin configuration, secrets, collaborators, webhooks and environment settings are outside scope. Discussions are disabled.

Resolve any relevant wiki or service-configuration gaps before relying on this package as a complete service-level prerequisite for deleting the source. Keep this archive branch and package permanently if the source is later removed.
