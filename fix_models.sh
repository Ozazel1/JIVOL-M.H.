#!/bin/bash

# Remove duplicate in FREE_MODELS
sed -i '/FREE_MODELS = \[/,/\]/{ /nousresearch\/nous-hermes-2-mixtral-8x7b-dpo"$/{ N; /\]/!D; }; }' JIVOL.py

# Check the result
echo "FREE_MODELS after fix:"
sed -n '/FREE_MODELS = \[/,/\]/p' JIVOL.py

