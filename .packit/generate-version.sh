#!/bin/sh

# Generate the version and echo it out
echo $(rpmspec -q --srpm --qf "%{VERSION}" .packit/rpmlint.spec)~git$(date +"%Y%m%d.%H%M%S").$(git rev-parse --short HEAD)
