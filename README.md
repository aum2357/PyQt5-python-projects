# 🤖 AI Login Gate System

A futuristic quantum-inspired security authentication system with ASCII art interface, built using PyQt5 and Python.

![Python](https://img.shields.io/badge/python-v3.7+-blue.svg)
![PyQt5](https://img.shields.io/badge/PyQt5-5.15+-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Platform](https://img.shields.io/badge/platform-windows%20%7C%20linux%20%7C%20macos-lightgrey.svg)

## ✨ Features

- 🚀 **Futuristic ASCII Art Interface** - Dynamic animated ASCII art display
- 🔐 **Quantum-Inspired Security** - Advanced authentication system with attempt tracking
- 🎨 **Dynamic Gradient Backgrounds** - Real-time color changing based on system state
- 🔊 **Text-to-Speech Feedback** - Voice announcements for all system states
- ⚡ **Real-time Animation System** - Smooth transitions and frame-based animations
- 🛡️ **Multi-layered Security Protocol** - Configurable password protection
- ℹ️ **Professional About Dialog** - Developer information and system details
- 🎭 **State-based Visual Effects** - Different themes for idle, success, and denied states

## 🖼️ Screenshots

### Main Interface
The main login interface features a futuristic ASCII art display with animated elements and a sleek password input field.

### Success State
When authentication succeeds, the system displays a green-themed success animation with congratulatory messages.

### Denied State
Failed authentication attempts trigger a red-themed warning display with security breach notifications.

## 🚀 Installation

### Prerequisites

- Python 3.7 or higher
- PyQt5
- pyttsx3 (for text-to-speech functionality)

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/AI_Login_Gate.git
   cd AI_Login_Gate
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python main.py
   ```

## 🔧 Configuration

### Password Settings
The default password is set to `"root"` and can be changed by modifying the `PASSWORD` variable in `main.py`:

```python
PASSWORD = "your_new_password"  # Change this to your desired password
```

### Attempt Limits
Maximum login attempts can be configured by changing the `MAX_ATTEMPTS` variable:

```python
MAX_ATTEMPTS = 3  # Change this to your desired limit
```

### Audio Settings
Text-to-speech settings can be customized in the `speak()` method to adjust voice rate, volume, and preferred voice selection.

## 🎮 Usage

1. **Launch the Application**
   - Run `python main.py` to start the AI Login Gate
   - The system will display the futuristic login interface

2. **Authentication**
   - Enter your password in the input field
   - Press Enter or wait for voice prompt
   - System provides real-time feedback for success/failure

3. **About Information**
   - Click the "ℹ️ ABOUT" button in the top-right corner
   - View developer information and system features

4. **System States**
   - **Idle**: Animated waiting state with scanning effects
   - **Success**: Green theme with access granted confirmation
   - **Denied**: Red theme with security breach warnings

## 🏗️ Project Structure

```
AI_Login_Gate/
├── main.py                 # Main application file
├── requirements.txt        # Python dependencies
├── config.json            # Configuration settings
├── test_voices.py         # Voice testing utility
├── .gitignore             # Git ignore file
├── README.md              # This file
└── __pycache__/           # Python cache (auto-generated)
```

## 🛠️ Technical Details

### Architecture
- **Frontend**: PyQt5 with custom styled widgets
- **Animation**: QTimer-based frame animations
- **Audio**: pyttsx3 text-to-speech engine
- **Graphics**: QGraphicsDropShadowEffect for glow effects

### Key Components
- `LoginWindow`: Main application window class
- `AnimatedLabel`: Custom animated label with glow effects
- `AboutDialog`: Professional information dialog
- `ASCII Art System`: Frame-based animation system

### Dependencies
- `PyQt5`: GUI framework
- `pyttsx3`: Text-to-speech functionality
- `sys`: System-specific parameters
- `os`: Operating system interface

## 🎨 Customization

### Themes
Colors can be customized by modifying the CSS-style strings in the `setStyleSheet()` methods:

```python
# Example: Change primary color from cyan to purple
border: 2px solid #00d4ff;  # Change to: border: 2px solid #9d4eff;
```

### ASCII Art
Custom ASCII art can be added by modifying the `get_ascii_art()` method:

```python
def get_ascii_art(self, art_type, frame=0):
    # Add your custom ASCII art here
    if art_type == "custom":
        return """Your custom ASCII art here"""
```

### Animations
Animation timing can be adjusted by modifying timer intervals:

```python
self.ascii_animation_timer.start(1000)  # Change interval (milliseconds)
```

## 📋 System Requirements

- **Operating System**: Windows 7+, macOS 10.12+, or Linux
- **Python**: Version 3.7 or higher
- **Memory**: 128 MB RAM minimum
- **Display**: 1400x800 minimum resolution recommended
- **Audio**: Speakers or headphones for voice feedback

## 🔒 Security Features

- **Attempt Tracking**: Monitors and limits login attempts
- **Session Management**: Automatic session termination after max attempts
- **Voice Feedback**: Audio confirmation for security events
- **Visual Indicators**: Color-coded status display
- **Lockdown Protocol**: System lockdown after failed attempts

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Development Setup
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Aditya Deep Ratnam Singh**
- Version: 0.0.1
- Date: July 20, 2025
- Technology: PyQt5 + Python

## 🙏 Acknowledgments

- PyQt5 development team for the excellent GUI framework
- pyttsx3 contributors for text-to-speech functionality
- ASCII art community for inspiration
- Quantum computing concepts for security theme inspiration

## 📞 Support

If you encounter any issues or have questions, please:
1. Check the existing issues on GitHub
2. Create a new issue with detailed description
3. Include your Python version and operating system

## 🔮 Future Enhancements

- [ ] Biometric authentication integration
- [ ] Database user management
- [ ] Network security protocols
- [ ] Mobile application version
- [ ] Advanced encryption algorithms
- [ ] Multi-language support
- [ ] Custom theme editor
- [ ] Plugin system architecture

---

*"Protecting Digital Frontiers with Style"* 🛡️

**⚠️ For authorized personnel only ⚠️**
