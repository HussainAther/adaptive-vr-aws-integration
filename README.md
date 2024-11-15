# Adaptive VR/AR with AWS Integration for Spatial Computing

## Overview
This project leverages **AWS Spatial Computing solutions** to create adaptive, immersive VR/AR educational experiences in real-time. The system integrates **Amazon Sumerian**, **AWS IoT TwinMaker**, and **Edge AI** to dynamically adjust content, haptic feedback, and user interactions, providing personalized learning experiences without constant cloud dependency.

### Key Features
- **Amazon Sumerian Integration**: Incorporates Sumerian’s AR/VR capabilities to deliver interactive 3D content and scenes directly in Unity, creating rich educational experiences.
- **AWS IoT TwinMaker for Real-World Simulation**: Allows real-world simulations and digital twin representations of complex environments, such as historical sites or scientific labs.
- **Edge AI Tutoring**: Runs AI models locally for low-latency adaptive feedback and personalized tutoring, making this accessible even without a constant internet connection.
- **Dynamic Haptic Feedback**: Provides real-time, context-aware haptic feedback that adjusts based on user interactions and comprehension levels.

## Project Structure

```plaintext
adaptive-vr-aws-integration/
├── AWSIntegration/                   # AWS scripts and configurations
│   ├── sumerian_project/             # Amazon Sumerian project files for VR/AR
│   ├── twinmaker_config/             # Configuration files for AWS IoT TwinMaker
│   ├── simulate_realworld.py         # Script for setting up simulations
│   └── aws_setup_instructions.md     # Documentation for AWS setup
├── EdgeModels/                       # Edge AI model training and optimization
│   ├── model_training.py             # Training script for edge-optimized model
│   ├── tutor_edge_model.tflite       # TensorFlow Lite model for Edge AI
│   └── model_optimization.md         # Instructions for model optimization
├── Assets/                           # VR/AR assets for Unity
│   ├── Scenes/                       # Scene files for testing AWS-integrated holograms
│   ├── Scripts/                      # Unity scripts for AWS and Edge AI integration
│   │   ├── EdgeAIController.cs       # Main controller for Edge AI model inference
│   │   ├── SumerianIntegration.cs    # Integration script for Amazon Sumerian
│   │   ├── TwinMakerIntegration.cs   # Integration script for IoT TwinMaker
│   │   └── AdaptiveFeedback.cs       # Script for delivering adaptive feedback
│   ├── Prefabs/                      # Prefabs for Edge AI-based tutoring and assets
│   └── Materials/                    # Materials for visual feedback cues
├── Documentation/                    # Project documentation
│   ├── README.md                     # Project overview and setup instructions
│   ├── ModelTraining.md              # Training and optimization for Edge AI model
│   ├── AWSIntegration.md             # Instructions for AWS service integration
│   └── EdgeSetup.md                  # Edge AI deployment setup guide
└── .gitignore                        # Ignore files for Unity, model files, etc.
```

## Getting Started

### Prerequisites
- **Unity** (2020 or newer)
- **AWS Account**: Required for setting up Amazon Sumerian and IoT TwinMaker.
- **Python** (3.6 or newer) with TensorFlow
- **TensorFlow Lite Plugin for Unity** (for Edge AI model deployment)

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/YOUR_USERNAME/adaptive-vr-aws-integration.git
   cd adaptive-vr-aws-integration
   ```

2. **AWS Services Setup**:
   - Follow instructions in `Documentation/aws_setup_instructions.md` to configure Amazon Sumerian and IoT TwinMaker services.
   - Set up any necessary roles, permissions, and project configurations within AWS.

3. **Unity Setup**:
   - Open the project in Unity.
   - Add the **TensorFlow Lite Plugin** to Unity to enable Edge AI model integration.
   - Place the `tutor_edge_model.tflite` file in Unity’s `StreamingAssets` folder to enable on-device predictions.

## AWS Services Integration

### Amazon Sumerian Integration
- **SumerianIntegration.cs**: This script handles the connection to Amazon Sumerian and loads 3D content directly in Unity.
- **Usage**: Place 3D assets in `sumerian_project/` and use `SumerianIntegration.cs` to dynamically render them within Unity.

### AWS IoT TwinMaker Integration
- **TwinMakerIntegration.cs**: Connects Unity holograms with real-world data and simulations from IoT TwinMaker.
- **Usage**: Configure digital twins in `twinmaker_config/` and load simulations in Unity using the integration script.

For detailed setup, refer to `Documentation/AWSIntegration.md`.

## Edge AI Integration for Adaptive Tutoring

### Model Training and Optimization
1. Run `EdgeModels/model_training.py` to train the model and export it as a `.tflite` file.
2. This model provides adaptive feedback based on user interactions, adjusting intensity and guidance to match comprehension levels.

### Unity Integration for Edge AI
- **EdgeAIController.cs**: This script runs the TensorFlow Lite model on-device to make real-time predictions based on user data.
- **AdaptiveFeedback.cs**: Adjusts the visual, auditory, or haptic feedback in response to AI predictions for an adaptive learning experience.

See `Documentation/ModelTraining.md` and `Documentation/EdgeSetup.md` for full details.

## Dynamic Haptic Feedback

**HapticIntegrationHandler.cs** in **Assets/Scripts** provides real-time, adaptive haptic feedback based on AI-driven predictions. Feedback intensity adjusts dynamically based on student comprehension, enabling a more interactive learning experience. 

## Contributing
We welcome contributions to improve the adaptive VR/AR learning experience. Please fork the repository, create a feature branch, and submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Enjoy creating adaptive, immersive educational experiences with AWS and Edge AI!
