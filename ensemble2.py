import argparse
import pickle
import os

import numpy as np
from tqdm import tqdm
from Confusion_Matrix import Confusion_Matrix
conf_mat = Confusion_Matrix(155)
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset',
                        required=True,
                        choices={'uav','ntu/xsub', 'ntu/xview', 'ntu120/xsub', 'ntu120/xset', 'NW-UCLA'},
                        help='the work folder for storing results')
    parser.add_argument('--alpha',
                        default=1,
                        help='weighted summation',
                        type=float)

    parser.add_argument('--joint-dir',
                        help='Directory containing "epoch1_test_score.pkl" for joint eval results')
    parser.add_argument('--bone-dir',
                        help='Directory containing "epoch1_test_score.pkl" for bone eval results')
    parser.add_argument('--joint-t-dir', default=None)
    parser.add_argument('--bone-t-dir', default=None)
    parser.add_argument('--k-t-dir', default=None)
    parser.add_argument('--indrnn-t-dir', default=None)
    parser.add_argument('--indrnn-b-dir', default=None)
    arg = parser.parse_args()

    dataset = arg.dataset
    if 'UCLA' in arg.dataset:
        label = []
        with open('./data/' + 'NW-UCLA/' + '/val_label.pkl', 'rb') as f:
            data_info = pickle.load(f)
            for index in range(len(data_info)):
                info = data_info[index]
                label.append(int(info['label']) - 1)
    elif 'ntu120' in arg.dataset:
        if 'xsub' in arg.dataset:
            npz_data = np.load('./data/' + 'ntu120/' + 'NTU120_CSub.npz')
            label = np.where(npz_data['y_test'] > 0)[1]
        elif 'xset' in arg.dataset:
            npz_data = np.load('./data/' + 'ntu120/' + 'NTU120_CSet.npz')
            label = np.where(npz_data['y_test'] > 0)[1]
    elif 'ntu' in arg.dataset:
        if 'xsub' in arg.dataset:
            npz_data = np.load('./data/' + 'ntu/' + 'NTU60_CS.npz')
            label = np.where(npz_data['y_test'] > 0)[1]
        elif 'xview' in arg.dataset:
            npz_data = np.load('./data/' + 'ntu/' + 'NTU60_CV.npz')
            label = np.where(npz_data['y_test'] > 0)[1]
    elif 'uav' in arg.dataset:
        npz_data = np.load('./data/' + 'uav2/' + 'y_test.npz')
        label = np.where(npz_data['y_test'] > 0)[1]
    else:
        raise NotImplementedError

    with open(os.path.join(arg.joint_dir, 'epoch1_test_score.pkl'), 'rb') as r1:
        r1 = list(pickle.load(r1).items())

    with open(os.path.join(arg.bone_dir, 'epoch1_test_score.pkl'), 'rb') as r2:
        r2 = list(pickle.load(r2).items())

    if arg.joint_t_dir is not None:
        with open(os.path.join(arg.joint_t_dir, 'epoch1_test_score.pkl'), 'rb') as r3:
            r3 = list(pickle.load(r3).items())
    if arg.bone_t_dir is not None:
        with open(os.path.join(arg.bone_t_dir, 'epoch1_test_score.pkl'), 'rb') as r4:
            r4 = list(pickle.load(r4).items())
    if arg.k_t_dir is not None:
        with open(os.path.join(arg.k_t_dir, 'epoch1_test_score.pkl'), 'rb') as r5:
            r5 = list(pickle.load(r5).items())
    if arg.indrnn_t_dir is not None:
        with open(os.path.join(arg.indrnn_t_dir, 'epoch1_test_score.pkl'), 'rb') as r6:
            r6 = list(pickle.load(r6).items())
    if arg.indrnn_b_dir is not None:
        with open(os.path.join(arg.indrnn_b_dir, 'epoch1_test_score.pkl'), 'rb') as r7:
            r7 = list(pickle.load(r7).items())
    right_num = total_num = right_num_5 = 0
    
   
    arg.alpha = [0.6, 0.6, 0.6, 0.6]
    for i in tqdm(range(len(label))):
        l = label[i]
        _, r11 = r1[i]
        _, r22 = r2[i]
        _, r33 = r3[i]
        _, r44 = r4[i]
        _, r55 = r5[i]
        _, r66 = r6[i]
        _, r77 = r7[i]
        r =0.55*r44+0.95*r33+0.65*r11+0.75*r22+0.55*r55+0.65*r66+r77 #+ r44 * arg.alpha[2] #+ r44 * arg.alpha[3]+ r22 * arg.alpha[1]
        rank_5 = r.argsort()[-5:]
        right_num_5 += int(int(l) in rank_5)
        r = np.argmax(r)
        right_num += int(r == int(l))
        total_num += 1
        acc = right_num / total_num
        acc5 = right_num_5 / total_num
        conf_mat.static_a_batch(r,l)
   # conf_mat.normalize()
    #conf_mat.show_mat()
   
    print('Top1 Acc: {:.4f}%'.format(acc * 100))
    print('Top5 Acc: {:.4f}%'.format(acc5 * 100))
