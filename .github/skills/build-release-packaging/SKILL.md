---
name: build-release-packaging
description: Build, version, package, and publish the QA-certified application into deployable release artifacts (binaries, container images, bundles) for the target platform, without altering the certified code. Use to produce the release before deployment.
---

# Build & Release Packaging

## Purpose

Turn the QA-certified source into a deployable, versioned, published release artifact — reproducibly and
without changing the certified code.

## Rules

- Build **only** the QA-certified commit/build; never alter application code here (a code change would
  invalidate certification → route back to Software Engineer + re-certify).
- Use the build/packaging approach implied by the approved stack (language toolchain, container build,
  bundler).
- **Version** the release traceably (e.g. semver + commit sha); the version appears in the Deployment
  Report.
- Produce artifacts appropriate to the target platform (container image, binary, static bundle, package).
- **Publish** to the approved registry/artifact store (image registry, package registry, artifact bucket)
  using credentials from the secret store — never embed credentials.
- Prefer reproducible builds; pin dependencies/base images.

## Method

1. Confirm the certified build id from `deployment-readiness-analysis`.
2. Run the build with the approved toolchain; fail fast on any build/lint/type error.
3. Package for the target; tag with the release version.
4. Publish to the approved registry/store; record the artifact's coordinates (name:tag/digest, URL).

## Output

Published, versioned release artifact(s) with their coordinates and how to pull them — feeds
`deploy-execution-verification` and the Deployment Report.

## Boundaries

- No source changes; no deploying (that is the deploy skill).
- No plaintext credentials for registries/stores.
