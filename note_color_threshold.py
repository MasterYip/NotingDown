'''
Author: MasterYip 2205929492@qq.com
Date: 2022-11-05 14:11:07
LastEditors: MasterYip 2205929492@qq.com
LastEditTime: 2023-06-09 21:18:05
FilePath: \comprehensive-coding\FastImgNotingDown\note_color_threshold.py
Description: 

Copyright (c) 2022 by MasterYip 2205929492@qq.com, All Rights Reserved. 
'''
#!/usr/bin/env python3
# coding=utf-8

import cv2
import numpy as np
from cv2 import (ADAPTIVE_THRESH_MEAN_C, COLOR_GRAY2RGB, COLOR_HSV2RGB,
                 COLOR_RGB2GRAY, COLOR_RGB2HSV, IMWRITE_PNG_COMPRESSION,
                 THRESH_BINARY, adaptiveThreshold, bitwise_not,
                 connectedComponents, connectedComponentsWithStats, cvtColor,
                 dilate, erode, imread, imwrite)
# from matplotlib.pyplot import imshow, subplot
from numpy import mean, ones, power, uint8


def imgInversionCheck(img, Thresh_dia=801):
    '''
    description: Check if the image is inverted.
    param {*} self
    param {*} img
    param {*} Thresh_dia
    return {*} True if the image is inverted.
    '''
    grey = cvtColor(img, COLOR_RGB2GRAY)
    thresh = adaptiveThreshold(
            grey, 255, ADAPTIVE_THRESH_MEAN_C, THRESH_BINARY,
            Thresh_dia, 0)
    mean_normal = mean(thresh) # Usually black when input is white
    thresh = adaptiveThreshold(
            bitwise_not(grey), 255, ADAPTIVE_THRESH_MEAN_C, THRESH_BINARY,
            Thresh_dia, 0)
    mean_inverse = mean(thresh)
    return mean_inverse > mean_normal

def note_color_threshold_for_white_bkg(img, sat_remap_order=0.5, dilate_rad=0,
                                       Thresh_bias=50, Thresh_dia=351, mode=0):
    # pre processing
    grey = cvtColor(img, COLOR_RGB2GRAY)
    thresh = adaptiveThreshold(
        grey, 255, ADAPTIVE_THRESH_MEAN_C, THRESH_BINARY,
        Thresh_dia, Thresh_bias)
    # (considering backgroud color, for cases like blacboard notes)
    if mean(thresh) > 127:
        thresh = bitwise_not(thresh)

    # Dilate handwriting
    if dilate_rad > 0:
        kernel = ones((dilate_rad, dilate_rad), uint8)
        thresh = dilate(thresh, kernel, iterations=1)
    elif dilate_rad < 0:
        kernel = ones((-dilate_rad, -dilate_rad), uint8)
        thresh = erode(thresh, kernel, iterations=1)

    if mode == 0:  # Black & White
        return bitwise_not(thresh)
    elif mode == 1:  # Recognize Color
        # Filter out handwritings
        num_objects, labels = connectedComponents(thresh, connectivity=8)

        # Increase Saturation of Origin Pic
        saturated_HSV = cvtColor(img, COLOR_RGB2HSV)
        saturated_HSV[:, :, 1] = power(
            saturated_HSV[:, :, 1]/255, sat_remap_order)*255
        img_sat_remap = cvtColor(saturated_HSV, COLOR_HSV2RGB)
        # filter out background
        img_sat_remap[labels == 0] = [255, 255, 255]

        # Combination (turn pixels which has low saturation to black)
        thresh_RGB = cvtColor(thresh, COLOR_GRAY2RGB)
        thresh_RGB = bitwise_not(thresh_RGB)
        thresh_RGB[saturated_HSV[:, :, 1] >
                   100] = img_sat_remap[saturated_HSV[:, :, 1] > 100]
        return thresh_RGB


def note_color_threshold_for_black_bkg(img, sat_remap_order=0.5, dilate_rad=0,
                                       Thresh_bias=50, Thresh_dia=351, mode=0):
    # pre processing
    img = bitwise_not(img)
    grey = cvtColor(img, COLOR_RGB2GRAY)
    thresh = adaptiveThreshold(
        grey, 255, ADAPTIVE_THRESH_MEAN_C, THRESH_BINARY,
        Thresh_dia, Thresh_bias)
    # (considering backgroud color, for cases like blacboard notes)
    if mean(thresh) > 127:
        thresh = bitwise_not(thresh)

    # Dilate handwriting
    if dilate_rad > 0:
        kernel = ones((dilate_rad, dilate_rad), uint8)
        thresh = dilate(thresh, kernel, iterations=1)
    elif dilate_rad < 0:
        kernel = ones((-dilate_rad, -dilate_rad), uint8)
        thresh = erode(thresh, kernel, iterations=1)

    if mode == 0:  # Black & White
        return bitwise_not(thresh)
    elif mode == 1:  # Recognize Color
        # Filter out handwritings
        num_objects, labels = connectedComponents(thresh, connectivity=8)

        # Increase Saturation of Origin Pic
        saturated_HSV = cvtColor(img, COLOR_RGB2HSV)
        saturated_HSV[:, :, 1] = power(
            saturated_HSV[:, :, 1]/255, sat_remap_order)*255
        img_sat_remap = cvtColor(saturated_HSV, COLOR_HSV2RGB)
        # filter out background
        img_sat_remap[labels == 0] = [255, 255, 255]

        # Combination (turn pixels which has low saturation to black)
        thresh_RGB = cvtColor(thresh, COLOR_GRAY2RGB)
        thresh_RGB = bitwise_not(thresh_RGB)
        thresh_RGB[saturated_HSV[:, :, 1] >
                   100] = img_sat_remap[saturated_HSV[:, :, 1] > 100]
        return thresh_RGB


def note_color_threshold(img, sat_remap_order=0.5,
                         dilate_rad=0, invert_threshold=127):
    # pre processing
    # (considering backgroud color, for cases like blacboard notes)
    if mean(img) > invert_threshold:  # 似乎需要更换更好的算法处理黑白 因为黑板亮度不好说（用直方图）
        img = bitwise_not(img)
    grey = cvtColor(img, COLOR_RGB2GRAY)
    thresh = adaptiveThreshold(
        grey, 255, ADAPTIVE_THRESH_MEAN_C, THRESH_BINARY, 351, 50)

    # Dilate handwriting
    kernel = ones((dilate_rad, dilate_rad), uint8)
    thresh = dilate(thresh, kernel, iterations=1)

    # Filter out handwritings
    num_objects, labels = connectedComponents(thresh, connectivity=8)

    # Increase Saturation of Origin Pic
    saturated_HSV = cvtColor(img, COLOR_RGB2HSV)
    saturated_HSV[:, :, 1] = power(
        saturated_HSV[:, :, 1]/255, sat_remap_order)*255
    img_sat_remap = cvtColor(saturated_HSV, COLOR_HSV2RGB)
    # filter out background
    img_sat_remap[labels == 0] = [255, 255, 255]

    # Combination (turn pixels which has low saturation to black)
    img_saturation = saturated_HSV[:, :, 1]
    thresh_RGB = cvtColor(thresh, COLOR_GRAY2RGB)
    thresh_RGB = bitwise_not(thresh_RGB)
    thresh_RGB[img_saturation > 100] = img_sat_remap[img_saturation > 100]
    return thresh_RGB


class BlackboardRecorder(object):
    graph_display = False

    def __init__(self, src_img):
        '''
        description: Preprocess src_img, including threshhold, Erode.\n
            self.thresh - for White Bkg img\n
            self.thresh_ivt - for Black Bkg img\n
        return None
        '''
        self.img = src_img
        self.erode_rad_rel = 0.005
        self.dilate_rad_rel = 0.005
        self.thresh_rad_rel = 1
        thresh_bias = 0

        # Thresh
        thresh_rad = int(self.thresh_rad_rel *
                         min(self.img.shape[:1])/2)*2+1  # must be odd
        self.grey = cvtColor(self.img, COLOR_RGB2GRAY)
        # for White Bkg
        self.thresh = adaptiveThreshold(self.grey, 255,
                                        ADAPTIVE_THRESH_MEAN_C, THRESH_BINARY,
                                        thresh_rad, thresh_bias)
        # for Black Bkg
        self.thresh_ivt = bitwise_not(self.thresh)

        # Erode
        erode_rad = int(self.erode_rad_rel*min(self.img.shape[:1]))+1
        erode_kernel = ones((erode_rad, erode_rad), uint8)  # 待改为圆形
        self.thresh = erode(self.thresh, erode_kernel, iterations=1)
        self.thresh_ivt = erode(self.thresh_ivt, erode_kernel, iterations=1)

        dilate_rad = int(self.dilate_rad_rel*min(self.img.shape[:1]))+1
        dilate_kernel = ones((dilate_rad, dilate_rad), uint8)  # 待改为圆形
        self.thresh = dilate(self.thresh, dilate_kernel, iterations=1)
        self.thresh_ivt = dilate(self.thresh_ivt, dilate_kernel, iterations=1)

    def find_possible_ROIs(self, thresh):
        '''
        description: find_possible_ROIs, temporarily support ONE target\n
        params:\n
            thresh\n
        return (src_points, dst_points, (dst_img_w, dst_img_h))
        '''
        num_labels, labels, stats, centroids = connectedComponentsWithStats(
            thresh, connectivity=4, ltype=None)
        if self.graph_display:
            subplot(1, 4, 1)
            imshow(thresh)

        # ===================有待改进
        def find_blackboard(num_labels, labels, stats, centroids):
            img_area = labels.shape[0]*labels.shape[1]
            id_list = []
            area_coef = 0.3
            img_area_coef = 0.1
            for i in range(1, stats.__len__()):
                if (stats[i][4] > area_coef*stats[i][2]*stats[i][3] and
                    stats[i][2]*stats[i][3] > img_area_coef*img_area and
                        stats[i][2]*stats[i][3] < img_area):
                    id_list.append(i)
                    print(i, stats[i])
            # 面积最大
            # TODO:Need to be fixed
            return id_list[stats[id_list, 4].argmax()]
        id = find_blackboard(num_labels, labels, stats, centroids)

        ROI = np.zeros(labels.shape, np.uint8)
        ROI[labels == id] = 255
        if self.graph_display:
            subplot(1, 4, 2)
            imshow(ROI)

        def get_polygon(labels, id):
            blank = np.zeros(labels.shape, dtype=np.uint8)
            blank[labels == id] = 255
            kernel = np.ones((5, 5), np.uint8)
            blank = cv2.dilate(blank, kernel, iterations=1)
            contours, hierarchy = cv2.findContours(
                blank, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            c0 = contours[0]
            # this para is important(decide the approximation,
            # i.e. the polygon edge numbers)
            coef = 0.005  # 0.05 default (Simpler when larger)
            epsilon = coef * cv2.arcLength(c0, True)
            approx = cv2.approxPolyDP(c0, epsilon, True)
            return approx

        approx = get_polygon(labels, id)
        draw_img = self.img.copy()
        res = cv2.drawContours(
            draw_img, [approx], -1, (255, 0, 0), int(draw_img.shape[0]/20))
        if self.graph_display:
            subplot(1, 4, 3)
            imshow(res)

        # print(approx[:,0])

        def find_angular_point(points):
            ang_pt = points[:4].copy()
            for pt in points:
                if pt.sum() < ang_pt[0].sum():
                    ang_pt[0] = pt.copy()
                if pt.sum() > ang_pt[2].sum():
                    ang_pt[2] = pt.copy()
                if pt[0]-pt[1] < ang_pt[1][0]-ang_pt[1][1]:
                    ang_pt[1] = pt.copy()
                if pt[0]-pt[1] > ang_pt[3][0]-ang_pt[3][1]:
                    ang_pt[3] = pt.copy()
            return ang_pt

        def wrap_size_est(ang_pt):
            img_h = int((np.linalg.norm(ang_pt[0]-ang_pt[1]) +
                         np.linalg.norm(ang_pt[2]-ang_pt[3]))/2)
            img_w = int((np.linalg.norm(ang_pt[1]-ang_pt[2]) +
                         np.linalg.norm(ang_pt[3]-ang_pt[1]))/2)
            return (img_w, img_h)

        src_points = find_angular_point(approx[:, 0])
        print(src_points)
        # target_img_shape = (img_w, img_h)
        img_w, img_h = wrap_size_est(src_points)
        print(img_w, img_h)
        dst_points = np.array([[0, 0], [0, img_h], [img_w, img_h], [img_w, 0]])
        return (src_points, dst_points, (img_w, img_h))

    def homography_projection(self, src_img, src_pt, dst_pt, dst_shape):
        H, _ = cv2.findHomography(src_pt, dst_pt)
        img_src_warp = cv2.warpPerspective(src_img, H, dst_shape)
        if self.graph_display:
            subplot(1, 4, 4)
            imshow(img_src_warp)
        return img_src_warp


def note_color_thershold_test():
    name = 'test.jpg'
    img = imread(name)
    thresh_color = note_color_threshold(img, 0.6, 2)
    imwrite('thresh_color.png', thresh_color, [IMWRITE_PNG_COMPRESSION, 9])


if __name__ == '__main__':
    bb = BlackboardRecorder()
    print(bb['erode_rad_rel'])
