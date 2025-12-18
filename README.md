# Malaria_Detection_Webapp

Detecting a cell image having malria or not of human.

# Project Overview

- The aim of this project is to focus on the first fundamental features of the decision making ability of an malaria detection web app, i.e., to develop a
deep learning model that reads infected and uninfected cells and classifies them correctly using Convolutional Neural Networks(CNNs).

- The images used in this work were whole slide images provided in the PEIR-VM repository built by the University of Alabama in Birmingham. The original whole slide image data contain significant amount of redundant information. In order to achieve good classification accuracy, image segmentation and de-noising are needed to extract only blood cells and remove those redundant image pixels simultaneously.
Several effective image processing techniques were used to accurately segment tiles into individual cells.

# Files Description

malaria_detection.ipynb
- Contains the whole notebook along with model building and data transformations process.
- Evaluation and model explanaibility is also given at the end of the notebook.

app.py
- predict(): Takes an image as input from the function parameter, preprocesses it and feeds it to the model for results.


requirements.txt
- This has all the dependencies required for deployment.


# Observations/Findings 
No Overfitting:

The absence of overfitting is a positive observation. Overfitting occurs when a model learns the training data too well, including its noise and outliers, to the extent that it performs poorly on unseen data. A lack of overfitting suggests that the model generalizes well to new, unseen data. This is a crucial aspect of model performance, ensuring that it doesn't memorize the training set but learns patterns that can be applied to different samples.

High Accuracy:
An accuracy score of 96.52% on the test dataset is a notable achievement. This indicates that the model is making correct predictions for the majority of the test samples. However, it's important to consider the class distribution in the dataset. If the classes are imbalanced (e.g., more samples of one class than the other), accuracy alone might not provide a complete picture. It's recommended to also evaluate precision, recall, and F1-score, especially in medical applications where the cost of false positives or false negatives can vary.

Correct Identification of Images:
The observation that the model is able to identify most of the images correctly is a positive sign of its effectiveness. It suggests that the features learned during training are relevant and discriminative for distinguishing between infected and uninfected cells. Visual inspection of a subset of predictions, along with their ground truth labels, can provide insights into the model's strengths and potential areas for improvement.

Confusion Matrix and Class-wise Metrics:
To gain a more detailed understanding of the model's performance, consider generating a confusion matrix. This matrix provides a breakdown of true positives, true negatives, false positives, and false negatives. From this, you can compute precision, recall, and F1-score for each class. These metrics can be particularly important in medical applications, where the consequences of false positives and false negatives can vary.

Threshold Tuning:
Depending on the application, you might explore tuning the classification threshold. The default threshold for binary classification is often 0.5, but adjusting it can impact the trade-off between sensitivity and specificity. In medical diagnosis, you may want to prioritize sensitivity (recall) to reduce false negatives, even at the cost of increased false positives.

Visualizing Model Predictions:
Consider visualizing model predictions on a subset of the test dataset. This can help identify specific patterns or types of images where the model may struggle. Techniques like Grad-CAM (Gradient-weighted Class Activation Mapping) can highlight the regions in the input images that are most influential in the model's decision-making process.

Model Interpretability:
In medical applications, it's important to have interpretable models. Consider using techniques like LIME (Local Interpretable Model-agnostic Explanations) or SHAP (SHapley Additive exPlanations) to explain individual predictions. This can enhance trust in the model's decisions, especially in critical domains like healthcare.in the above i used LIME.



