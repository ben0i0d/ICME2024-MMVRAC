# 2024-MMVRAC

SUBMIT-CODE REPO

This repository is no longer maintained, it has been moved to archive status, the following is the ICME2024 (MMVRAC) TOP repository, please refer to their work

https://github.com/liujf69/ICMEW2024-Track10

## RESULT

## cross-subject1
```
Top1 Acc: 47.4394%
Top5 Acc: 66.9891%
```
## cross-subject2
```
Top1 Acc: 74.2840%
Top5 Acc: 93.7566%
```
# HOW TO TEST MY CODE (ONLY TEST NOT TRAIN)

## INSTAL LIB

`pip install -r numpy tqdm`

## cross-subject1 Testing

`python ensemble.py --dataset uav --joint-dir work_dir/uav/test_joint --bone-dir work_dir/uav/test_jm --joint-t-dir work_dir/uav/k1 --bone-t-dir work_dir/uav/k4 --k-t-dir work_dir/uav/ctrgcn_bone_t --indrnn-t-dir work_dir/uav/shift1 `

## cross-subject2 Testing
`python ensemble2.py --dataset uav --joint-dir work_dir/uav2/k --bone-dir work_dir/uav2/j --joint-t-dir work_dir/uav2/k1 --bone-t-dir work_dir/uav2/k4 --k-t-dir work_dir/uav2/bone --indrnn-t work_dir/uav2/shift1 --indrnn-b work_dir/uav2/shift2`

# if your need model and config

To avoid the repository becoming too large, I deleted unnecessary files within the 'work_dir'. I have compressed the original directory and uploaded it to Google Drive. If you need it, please download the compressed file and replace the 'work_dir'. 

https://drive.google.com/file/d/1zyXsPwSC9r38TlC4luQ0jVjboQWW_QVV/view?usp=drive_link

Additionally, if you have any questions, please send an email to my email address, I will respond as soon as possible.