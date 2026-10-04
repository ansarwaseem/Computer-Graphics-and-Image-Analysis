# ============================================================
# IMAGE FILTERING USING PYTHON
# Average Filter, Weighted Mean Filter, and Laplacian Filter
# ============================================================


# ------------------------------------------------------------
# 1. IMPORT REQUIRED LIBRARIES
# ------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

from PIL import Image
from scipy import ndimage


# ------------------------------------------------------------
# 2. LOAD THE IMAGE
# ------------------------------------------------------------

# Open the image file.
# Make sure "MyImg.jpeg" is in the same folder as this notebook.
image = Image.open("MyImg.jpeg")

# Display some basic information about the image.
print("Image mode:", image.mode)
print("Image size:", image.size)


# ------------------------------------------------------------
# 3. CONVERT THE IMAGE TO GRAYSCALE
# ------------------------------------------------------------

# "L" converts the image into grayscale.
# A grayscale image contains only intensity values:
# 0   = Black
# 255 = White
gray_image = image.convert("L")


# Display the grayscale image.
plt.imshow(gray_image, cmap="gray")
plt.axis("off")
plt.show()


# ------------------------------------------------------------
# 4. CONVERT THE IMAGE INTO A NUMPY ARRAY
# ------------------------------------------------------------

# Convert the grayscale image into a NumPy array.
# This allows us to perform mathematical operations
# on the individual pixel values.
gray_array = np.array(gray_image)

# Display the array information.
print("Array shape:", gray_array.shape)
print("Data type:", gray_array.dtype)


# ------------------------------------------------------------
# 5. CHECK A SMALL PART OF THE IMAGE ARRAY
# ------------------------------------------------------------

# Display the first 5 rows and first 5 columns
# of the image array.
print(gray_array[:5, :5])


# ------------------------------------------------------------
# 6. CONVERT PIXELS FROM UINT8 TO FLOAT32
# ------------------------------------------------------------

# The original grayscale image uses uint8.
#
# uint8 can store values only from 0 to 255.
# During filtering, mathematical calculations can produce
# values greater than 255 or negative values.
#
# Therefore, we convert the image to float32 before filtering.
gray_array_float = gray_array.astype(np.float32)

print("Data type after conversion:", gray_array_float.dtype)


# ============================================================
# 7. AVERAGE / MEAN FILTER
# ============================================================

# Create a 3x3 average filter kernel.
#
# Every pixel in the 3x3 neighborhood has equal importance.
average_kernel = np.array([
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
])


# The kernel contains 9 values.
# Therefore, after calculating the sum of products,
# we divide by 9 to calculate the average.
average_kernel_sum = average_kernel.sum()

print("Average kernel sum:", average_kernel_sum)


# Apply convolution using the average kernel.
#
# mode="constant" means that pixels outside the image
# are treated as 0.
#
# cval=0 specifies that the constant value is 0.
average_filtered = ndimage.convolve(
    gray_array_float,
    average_kernel,
    mode="constant",
    cval=0
)


# Divide the convolution result by 9
# to convert the sum into an average.
average_filtered = average_filtered / average_kernel_sum


# Check the result.
print("Average Filter:")
print("Minimum:", average_filtered.min())
print("Maximum:", average_filtered.max())
print("Data type:", average_filtered.dtype)


# Display the average-filtered image.
plt.imshow(average_filtered, cmap="gray")
plt.axis("off")
plt.show()


# ============================================================
# 8. WEIGHTED MEAN FILTER
# ============================================================

# Create a weighted mean filter kernel.
#
# The center pixel has the highest weight.
# Therefore, the center has more influence on the result
# than the surrounding pixels.
weighted_kernel = np.array([
    [1, 2, 1],
    [2, 4, 2],
    [1, 2, 1]
])


# Calculate the total of all weights.
#
# 1 + 2 + 1
# 2 + 4 + 2
# 1 + 2 + 1
#
# Total = 16
weighted_kernel_sum = weighted_kernel.sum()

print("Weighted kernel sum:", weighted_kernel_sum)


# Apply convolution using the weighted kernel.
weighted_filtered = ndimage.convolve(
    gray_array_float,
    weighted_kernel,
    mode="constant",
    cval=0
)


# Divide by the sum of the weights.
# This converts the weighted sum into a weighted average.
weighted_filtered = weighted_filtered / weighted_kernel_sum


# Check the result.
print("Weighted Mean Filter:")
print("Minimum:", weighted_filtered.min())
print("Maximum:", weighted_filtered.max())
print("Data type:", weighted_filtered.dtype)


# Display the weighted-filtered image.
plt.imshow(weighted_filtered, cmap="gray")
plt.axis("off")
plt.show()


# ============================================================
# 9. LAPLACIAN FILTER
# ============================================================

# Create the Laplacian kernel from the assignment.
#
#       0   1   0
#       1  -4   1
#       0   1   0
#
# The Laplacian filter is mainly used for detecting
# rapid changes in intensity, which helps identify edges.
laplacian_kernel = np.array([
    [0, 1, 0],
    [1, -4, 1],
    [0, 1, 0]
])


# Check the sum of the Laplacian kernel.
#
# 0 + 1 + 0
# 1 - 4 + 1
# 0 + 1 + 0
#
# Kernel sum = 0
print("Laplacian kernel sum:", laplacian_kernel.sum())


# ------------------------------------------------------------
# APPLY THE LAPLACIAN FILTER
# ------------------------------------------------------------

# Apply convolution using the Laplacian kernel.
#
# mode="reflect" means that the values at the edges
# are reflected instead of adding artificial zero values.
#
# We use reflection because this is the edge-handling
# method specified in the assignment.
laplacian_filtered = ndimage.convolve(
    gray_array_float,
    laplacian_kernel,
    mode="reflect"
)


# IMPORTANT:
# We DO NOT divide the Laplacian result by the kernel sum.
#
# The Laplacian kernel has a sum of 0, but it is NOT an
# averaging filter. Its purpose is to detect changes
# in intensity.
#
# Therefore, the convolution result itself is the
# Laplacian-filtered output.


# Check the Laplacian result.
print("Laplacian Filter:")
print("Minimum:", laplacian_filtered.min())
print("Maximum:", laplacian_filtered.max())
print("Data type:", laplacian_filtered.dtype)


# ------------------------------------------------------------
# DISPLAY THE RAW LAPLACIAN RESULT
# ------------------------------------------------------------

# Display the actual Laplacian output.
#
# The result contains both positive and negative values.
# Because most smooth areas have values close to zero,
# the image may appear mostly dark or gray.
plt.imshow(laplacian_filtered, cmap="gray")
plt.axis("off")
plt.show()


# ============================================================
# 10. ABSOLUTE VALUE FOR LAPLACIAN VISUALIZATION
# ============================================================

# Take the absolute value of the Laplacian result.
#
# This converts:
# Negative values -> Positive values
#
# It allows us to visualize both positive and negative
# edge responses as brightness.
#
# IMPORTANT:
# This is ONLY for visualization.
# The original Laplacian result is still stored in
# "laplacian_filtered".
laplacian_display = np.abs(laplacian_filtered)


# Display the absolute-value Laplacian image.
plt.imshow(laplacian_display, cmap="gray")
plt.axis("off")
plt.show()


# ============================================================
# END OF IMAGE FILTERING
# ============================================================