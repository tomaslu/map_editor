#!/bin/bash
#
# Helper script that deletes database and migration if migrations should be
# tested from scratch.
#
# Start from within misc/ directory

echo Deleting database...
rm ../db.sqlite3

echo Deleting migrations...
rm -rf ../map/migrations/
