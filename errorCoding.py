import math
import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import os


class ErrorCorrection:
    def __init__(self, ):
        pass

    # get Average Length of the problem statement
    def _l_ave(self, probability_np, rint=False) -> np:
        """[get Average Length of the problem statement]
        Args:
            probability_np: probability's numpy
            rint: if np.rint required, it is for really problems such as the number of people which can be 1,2,3..n, when rint = false, L_ave equal entropy
        """
        reciprocal_value = np.reciprocal(probability_np)
        # print(f"reciprocal:{reciprocal_value}")
        # print(f"log:{_value1}")
        if rint:
            _value1 = np.log(reciprocal_value)+0.5
            _value1 = np.rint(_value1)
        else:
            _value1 = np.log(reciprocal_value)
            # print(f"log rint:{_value1}")
        _value2 = _value1*probability_np
        _lave = np.sum(_value2)
        return _lave

    def _entropy(self, probability_np):
        """[get entropy of the problem statement]
        Args:
            probability_np: probability's numpy
        """
        reciprocal_value = np.reciprocal(probability_np)
        _value1 = np.log(reciprocal_value)
        _value2 = _value1*probability_np
        _lave = np.sum(_value2)
        return _lave

    def _D_ary_huffman_code(self, probability_np, D_ary):
        """[get entropy of the problem statement]
        Args:
            probability_np ([np]): [probability_np: probability's numpy]
            D_ary([int]): the dimension(byte) of symbel
        """
        reciprocal_value = np.reciprocal(probability_np)
        _value_log = np.log(reciprocal_value)
        # print(f"[_D_ary_huffman_code]{_value_log}")
        _value1 = np.power(D_ary, _value_log)
        # print(f"[_D_ary_huffman_code]{_value1}")
        _value2 = np.reciprocal(_value1)
        # print(f"[_D_ary_huffman_code]{_value2}")
        _lave = np.sum(_value2)
        # print(f"[_D_ary_huffman_code]{_lave}")
        return _lave

    def _create_video(self, data_np, index_np, xlim, step=1, method=0,ylim=(0,10)):
        """[create a video to demenstorate the data_np]

        Args:
            data_np ([np]): [using data1 for drawing]
            index_np ([type]): [using data2 for drawing]
            xlim ([type]): [xlim]
            step (int, optional): [xlim's step]. Defaults to 1.
            method (int, optional): [method for using data_np and index_np]. Defaults to 0.
            ylim (tuple, optional): [ylim] Defaults to (0,10).
        """
        if os.path.exists("./temp_displayArray"):
            os.system("rm -rf ./temp_displayArray")
        os.mkdir("./temp_displayArray")
        min_value, max_value = xlim
        quantity = max_value/step-min_value/step
        plt.rcParams['axes.facecolor'] = 'black'
        fig = plt.figure(figsize=(10, 6), dpi=300, facecolor='black')
        ax = fig.add_subplot(111)
        ymin,ymax = ylim
        plt.xlim(min_value, max_value-min_value)
        plt.ylim(ymin, ymax)
        for spine in ['top', 'right', "bottom", "left"]:
            ax.spines[spine].set_color("white")
        ax.set_xlabel('Dimension')
        ax.set_ylabel('Length ')
        ax.xaxis.label.set_color('white')
        ax.yaxis.label.set_color('white')
        ax.tick_params(axis='x', colors="white")
        ax.tick_params(axis='y', colors="white")
        for j in range(min_value, int(quantity)):
            displayArray = np.array([])
            count = 0
            for i in range(min_value, j+1):
                count=count+1
                displayArray = np.append(displayArray, method(data_np, index_np[i]))
            max_value = min_value+step*count
            # print("min_value="+str(min_value)+" max_value="+str(max_value))
            _x_axis = np.arange(min_value, max_value+step/2,step)
            # print(_x_axis)
            _x_axis = _x_axis[:-1]
            # print(_x_axis)
            ax.plot(_x_axis,displayArray, color="white")
            plt.savefig(f'./temp_displayArray/displayArray_{str(j).zfill(10)}.png')
        if os.path.exists("out.mp4"):
            os.remove("out.mp4")
        os.system(f"ffmpeg -r 60 -f image2 -s 1920x1080 -pattern_type glob  -i './temp_displayArray/displayArray_*.png' -vcodec libx264 -crf 18  -pix_fmt yuv420p out.mp4")
        if os.path.exists("./temp_displayArray"):
            os.system("rm -rf ./temp_displayArray")

def main():
    probability_np = np.array([2/5, 3/5])
    ec = ErrorCorrection()
    print(ec._l_ave(probability_np))
    probability_np = np. array([8/23, 6/23, 4/23, 2/23, 2/23, 1/23])
    print(ec._l_ave(probability_np, True))
    probability_np = np.array([0.5, 0.25, 0.125, 0.125])
    print(ec._entropy(probability_np))

    if os.path.exists("./temp_displayArray"):
        os.system("rm -rf ./temp_displayArray")
    os.mkdir("./temp_displayArray")
    min_value = 2
    max_value = 20
    step = 0.1
    index_np = np.arange(min_value, max_value, step)
    ec._create_video(probability_np, index_np, (min_value,max_value), step, ec._D_ary_huffman_code,ylim=(0,2))

    # for j in range(min_value, int(quantity),(min_value,max_value),step,ec._D_ary_huffman_code):
    #     displayArray = np.array([])
    #     for i in range(min_value,j+1):
    #         displayArray = np.append(displayArray,ec._D_ary_huffman_code(probability_np,index_np[i]))
    #         # print(f"D={i}:{ec._D_ary_huffman_code(probability_np,i)}")
    #         # print(displayArray)
    #     plt.rcParams['axes.facecolor'] = 'black'
    #     fig = plt.figure(figsize=(10, 6), dpi=300,facecolor='black')
    #     ax = fig.add_subplot(111)
    #     plt.xlim(0,max_value)
    #     plt.ylim(0,2)
    #     for spine in ['top', 'right',"bottom","left"]:
    #         ax.spines[spine].set_color("white")
    #     ax.set_xlabel('Dimension')
    #     ax.set_ylabel('Length ')
    #     ax.xaxis.label.set_color('white')
    #     ax.yaxis.label.set_color('white')
    #     ax.tick_params(axis='x',colors = "white")
    #     ax.tick_params(axis='y',colors = "white")
    #     ax.plot(np.arange(2,displayArray.size+2),displayArray,color="white")
    #     plt.savefig(f'./temp_displayArray/displayArray_{str(j).zfill(10)}.png')
    # if os.path.exists("out.mp4"):
    #     os.remove("out.mp4")
    # os.system(f"ffmpeg -r 60 -f image2 -s 1920x1080 -pattern_type glob  -i './temp_displayArray/displayArray_*.png' -vcodec libx264 -crf 18  -pix_fmt yuv420p out.mp4")
    # plt.show()
if __name__ == '__main__':
    main()
