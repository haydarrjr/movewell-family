# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |

## Reporting a Vulnerability

The Movewell Family team takes security and privacy very seriously, especially given the health and movement context of our platform.

If you discover a security vulnerability or sensitive leak in this repository:

1. **Do NOT open a public GitHub issue.**
2. Report the vulnerability privately by emailing security@movewellfamily.org or submitting a private vulnerability disclosure on GitHub.
3. Include detailed steps to reproduce the issue, proof-of-concept code, and affected components.

## Security Practices
- **Zero Secret Commits**: Automated CI checks scan every pull request for accidental secret exposure.
- **Clinical Safety Hardguards**: All exercise recommendations pass through deterministic safety policy checks before being presented to users.
- **Privacy First**: Health and movement metrics remain on local hardware or within user-controlled Home Assistant environments.
