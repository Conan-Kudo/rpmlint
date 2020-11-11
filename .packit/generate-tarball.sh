#!/bin/sh

# Generate the versioned tarball
PACKAGE_VERSION=$(.packit/generate-version.sh)

git archive -o "rpmlint-${PACKAGE_VERSION}.tar.gz" --prefix "rpmlint-${PACKAGE_VERSION}/" HEAD
