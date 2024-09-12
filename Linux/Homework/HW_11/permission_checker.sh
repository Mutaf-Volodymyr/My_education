#!/bin/bash
set -e

ls -la /opt/290724-ptm | awk '{print $1}'
chmod 744 /opt/290724-ptm/*.sh

