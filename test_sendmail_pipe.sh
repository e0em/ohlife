#!/usr/bin/env zsh
conda env list
conda activate ohlife
which python
cat ./tmp.sample/sample_image.eml| python sendmail_pipe.py text
conda deactivate
