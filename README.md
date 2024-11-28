# Image processing

![Version](https://img.shields.io/badge/version-1.0.0-brightgreen.svg)

## Table of Contents

- [Introduction](#introduction)
- [Implement](#Implement)

## Introduction
In this package, we aim to use multiple image processing techniques to implement activation in the picture.Below are the contexts for reference
1. Binary with average value.
2. Blur
3. Chang color from RGB to Gray
4. Median filter

## Implement

### 1. Chang color from RGB to Gray<br>
   conver image color from RGB to Gray 
<div align=center><img src="https://github.com/user-attachments/assets/ee4020ed-8d35-42ed-8465-801484e84aad" width = "49%" height = width></div><br>
  
### 2. Binary with average value.<br>
Get the threshold from the image using the average value and perform binary conversion. If a pixel value is higher than the threshold, set it to 255; if not, set it to 0.
<div align=center><img src="https://github.com/user-attachments/assets/89720be0-27be-4a91-942e-64c4f64e4ac9" width = "49%" height = width></div><br>
  
### 3. Blur 3X3 <br>
It works like a convolution: if a 3X3 kernel is given, it will calculate the average using the kernel.
<div align=center><img src="https://github.com/user-attachments/assets/400d1d09-b7e4-4804-9183-7f63450a0f40" width = "49%" height = width></div><br>
  
### 4.Median filter 3X3 <br>
It works like blurring; however, instead of averaging the values, it uses the center value of the kernel as the result.
<div align=center><img src="https://github.com/user-attachments/assets/02ed5527-9f75-4544-afa4-73f8794ab740" width = "49%" height = width></div><br>
