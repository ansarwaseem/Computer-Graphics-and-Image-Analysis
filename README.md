# Computer Graphics and Image Analysis - MPhil Course

Welcome to my repository for the **Computer Graphics and Image Analysis** course. This repository documents my learning journey and projects completed during my MPhil studies, focusing on image processing, computer graphics, and deep learning applications.

## 📚 Course Overview

This course covers fundamental concepts and practical implementations in:
- **Image Filtering**: Applying various filter techniques to images
- **Image Processing**: Manipulating images as mathematical matrices
- **Computer Graphics**: Working with pixel-level operations and transformations
- **Deep Learning**: Building and training Convolutional Neural Networks for image classification

## 🔧 Projects Completed

### 1. **Image Filtering** 📁 `/Filtering`
Implemented and explored three different image filtering techniques:

- **Blur Filter**: Smooths image content by averaging pixel values
- **Sharpen Filter**: Enhances edges and details in images
- **Edge Detection Filter**: Identifies boundaries and transitions in images

Each filter was applied to sample images to demonstrate the effects of kernel-based convolution operations on image data.

**Key Concepts**:
- Convolution operations
- Kernel matrices
- Neighborhood operations

### 2. **Image as Matrix Multiplication** 📁 `/Img as Matrix Multi`
Performed matrix multiplication operations on image data:

- Converted an **8×8×1 image** into a matrix format
- Applied matrix multiplication for image transformation
- Demonstrated how images can be represented and manipulated as mathematical matrices

**Key Concepts**:
- Image representation as numerical matrices
- Linear algebraic transformations
- Pixel value computations through matrix operations

### 3. **CNN with DataSet Test Run** 📁 `/CNN with DataSet Test Run`
Built and trained a **Convolutional Neural Network (CNN)** for clothing and fashion item classification:

**What We Did**:
- **Downloaded FashionMNIST Dataset**: 60,000 training images and 10,000 test images of various clothing items
- **Built a Custom CNN Architecture**: 
  - Input: Grayscale images (28×28 pixels)
  - Conv2D Layer: 1 input channel → 16 feature maps with 3×3 kernel
  - ReLU Activation: Introduces non-linearity
  - Max Pooling: Reduces feature map size from 28×28 to 14×14
  - Fully Connected Layer: 16×14×14 features → 10 output classes
- **Trained the Model**: 2 epochs using Adam optimizer with CrossEntropyLoss
- **Achieved 88.62% Accuracy**: On unseen test data
- **Tested on Custom Images**: Fed real-world images (hoodie.jpg, sneakers.jpeg) to the trained model and predicted clothing categories

**Model Can Predict**:
- T-Shirt, Trouser, Pullover, Dress, Coat, Sandal, Shirt, Sneaker, Bag, Ankle Boot

**Key Concepts**:
- Convolutional Neural Networks (CNN)
- Feature extraction and pattern recognition
- Supervised learning and image classification
- Model training, validation, and testing
- Transfer of learned patterns to real-world images
- Image preprocessing (resizing, normalization, grayscale conversion)

## 📊 Folder Structure & Progression

Each folder represents a progression in the course, building upon concepts learned previously:

```
Computer-Graphics-and-Image-Analysis/
├── Filtering/                           # Basics: Understanding convolution & kernels
│   ├── blur_filter.py
│   ├── sharpen_filter.py
│   ├── edge_detection_filter.py
│   └── sample_results/
│
├── Img as Matrix Multi/                 # Intermediate: Linear algebra & transformations
│   ├── matrix_multiplication.py
│   ├── image_transformation.py
│   └── sample_images/
│
├── CNN with DataSet Test Run/           # Advanced: Deep learning & neural networks
│   ├── Task2_DataSet.ipynb              # Main CNN implementation
│   ├── OutPut.png                       # Sample prediction output
│   ├── hoodie.jpg                       # Test image 1
│   ├── sneakers.jpeg                    # Test image 2
│   └── data/                            # FashionMNIST dataset (auto-downloaded)
│
├── README.md
└── .gitignore
```

### Progression Overview:
1. **Filtering**: Learn how images can be manipulated using mathematical operations (kernels)
2. **Image as Matrix**: Understand images as numerical data and matrix transformations
3. **CNN with DataSet**: Apply deep learning to solve real image classification problems

## 🛠️ Technologies & Tools

- **Python 3.14+**: Primary programming language
- **PyTorch**: Deep learning framework
- **TorchVision**: Computer vision utilities and datasets
- **NumPy**: Numerical computing and matrix operations
- **OpenCV / PIL/Pillow**: Image processing and manipulation
- **Jupyter Notebooks**: Interactive code development and documentation
- **Matplotlib**: Data visualization and result display

## 🚀 Getting Started & Running the Code

### Prerequisites

Install all required dependencies:

```bash
pip install numpy opencv-python matplotlib pillow jupyter torch torchvision torchaudio
```

Or install using the requirements file (if available):
```bash
pip install -r requirements.txt
```

### Running the Code in Jupyter Notebook

1. **Clone the repository**:
```bash
git clone https://github.com/ansarwaseem/Computer-Graphics-and-Image-Analysis.git
cd Computer-Graphics-and-Image-Analysis
```

2. **Start Jupyter Notebook**:
```bash
jupyter notebook
```

3. **Navigate to a project folder and open the notebook**:
   - For **Filtering**: Open notebooks in `/Filtering/`
   - For **Image as Matrix**: Open notebooks in `/Img as Matrix Multi/`
   - For **CNN**: Open `Task2_DataSet.ipynb` in `/CNN with DataSet Test Run/`

4. **Run cells sequentially** (Shift + Enter):
   - The notebook will automatically download datasets if needed
   - Follow the comments and markdown cells for guidance
   - Outputs and visualizations will display below each cell

### Running the Code in VS Code

1. **Clone and navigate to the repository** (same as above)

2. **Install Jupyter extension in VS Code**:
   - Open VS Code
   - Go to Extensions (Ctrl+Shift+X)
   - Search for "Jupyter" and install the official extension

3. **Open a notebook file** (`.ipynb`):
   - Right-click on any `.ipynb` file
   - Select "Open with VS Code"
   - Click the play button (▶️) on each cell to execute

4. **Run Python scripts directly** (if `.py` files available):
```bash
python script_name.py
```

### Tips for Running Notebooks:

- **First Run**: The CNN notebook will download the FashionMNIST dataset (~30MB) automatically
- **GPU Support**: If you have CUDA-compatible GPU, PyTorch will use it automatically
- **Restart Kernel**: If you encounter issues, restart the kernel: Kernel → Restart Kernel
- **Check Dependencies**: Ensure all libraries are installed before running
- **File Paths**: Make sure image files (hoodie.jpg, sneakers.jpeg) are in the same folder as the notebook

## 📈 Course Progress

This repository will continue to be updated as the course progresses. New assignments, projects, and implementations will be added regularly to document:

- Advanced CNN architectures (ResNet, VGG, etc.)
- Transfer learning with pre-trained models
- Frequency domain processing (FFT, DCT)
- Color space transformations
- Image enhancement and restoration
- Morphological operations
- Object detection and segmentation
- Generative models (GANs, VAE)
- And more...

## 📝 Learning Outcomes

Through this course, I'm developing expertise in:
- ✅ Understanding image representation and manipulation
- ✅ Implementing classical image processing algorithms
- ✅ Building and training deep neural networks
- ✅ Working with NumPy and PyTorch for efficient computations
- ✅ Visualizing and analyzing image processing and ML results
- ✅ Applying linear algebra and calculus to real-world problems
- ✅ Preprocessing and preparing data for machine learning
- ✅ Model evaluation and performance optimization

## 📞 Contact & Connect

I'm always open to discussing computer graphics, image processing, deep learning, and related technologies!

- **Email**: [ansarwaseem313@gmail.com](mailto:ansarwaseem313@gmail.com)
- **LinkedIn**: [Ansar Waseem](https://www.linkedin.com/in/ansar-waseem/)
- **GitHub**: [@ansarwaseem](https://github.com/ansarwaseem)
- **Portfolio**: [Ansar Waseem - Portfolio](https://ansarwaseem.github.io/Ansar-Waseem-Portfolio/)

## 📄 License

© Ansar Waseem. All rights reserved.

This work is protected by copyright. Unauthorized copying, distribution, or modification is strictly prohibited. For permission to use this project, please contact the owner directly.

For inquiries, please contact: [ansarwaseem313@gmail.com](mailto:ansarwaseem313@gmail.com)

## ⭐ Acknowledgments

- My MPhil course instructors and peers
- PyTorch and TorchVision communities
- OpenCV and NumPy communities
- Online resources and tutorials that helped in understanding image processing and deep learning concepts
- FashionMNIST Dataset creators

---

**Last Updated**: October 2026

We will continue pushing different tasks and code implementations as we progress through this course.

Feel free to explore the projects, and don't hesitate to reach out with questions or suggestions!
