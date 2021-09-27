"""
======================================
Running pcarpet on human fMRI data
======================================

We we run-though some example data, to demonstrate the
functionality of pcarpet.
"""

# libraries
import os
import sys
# pcarpet functions
pcarpet_path = os.path.join(os.path.dirname(os.getcwd()), 'pcarpet')
sys.path.insert(0, pcarpet_path)
import pcarpet

###############################################################################
# Setting up paths
# ----------------
#
# First, let's define some input/output paths.
# pcarpet needs 3 paths to be specified:
#. fMRI file: a 4d nifti file, ideally minimally preprocessed.
#. Mask file: a 3d nifti file, binary mask defining the region-of-interest (e.g. cortex)
#. Output directory: for storing the outputs generated by pcarpet
# The fMRI and Mask files need to be in the same space, with identical x-y-z dimensions

# Path to folder containing example data
example_folder = '/home/niko/MRI/pcarpet_example'
# Path to preprocessed fMRI file
func = os.path.join(example_folder, 'func_preproc.nii.gz')
# Path to a cortical mask
cortex_mask = os.path.join(example_folder, 'cortex_mask.nii.gz')
# Path to a folder for storing the outputs
output_folder = os.path.join(example_folder, 'outputs')
