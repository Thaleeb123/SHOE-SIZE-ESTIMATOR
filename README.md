# 👟 Shoe Size Estimator 👟

## 📌 Overview
This project is a Python application that uses **OpenCV** to estimate the size of a shoe from an image. The application reads an image of a shoe, processes it, and calculates the size of the shoe in inches and UK shoe size.

## 📚 Dependencies
- **Python**
- **OpenCV**
- **NumPy**

## 🚀 How it Works
The application works by performing the following steps:
1. **Reads an image** of a shoe.
2. Converts the image to **grayscale**.
3. Detects the edges in the grayscale image using the **Canny edge detection** method.
4. Finds **contours** in the edge image.
5. Sorts the contours by area and keeps the largest two (assuming these are the shoes).
6. For each contour (shoe), it calculates the bounding rectangle and uses this to calculate the size of the shoe in pixels.
7. Converts the size from pixels to inches using a reference width.
8. Converts the size from inches to UK shoe size using a formula.

## 💻 Code
The main code for the application is contained in a single Python script. The script defines a function for calculating the distance between two points, which is used to calculate the size of the shoe. The script then reads an image, processes it, and calculates the shoe size.

## 📖 Usage
To use the application, simply run the Python script and pass the path to an image of a shoe as a command-line argument. The application will display the original image and the edge image, and print the estimated shoe size to the console.

## 🌟 Future Work
Future enhancements to this application could include improving the accuracy of the shoe size estimation, adding support for different shoe types, or adding a graphical user interface.

## 📝 License
This project is licensed under the MIT License. See the LICENSE file for details.
