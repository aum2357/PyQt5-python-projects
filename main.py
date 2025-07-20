import sys
import os
import pyttsx3
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QGraphicsDropShadowEffect, QSizePolicy, QTextEdit, QPushButton, QDialog, QTextBrowser
from PyQt5.QtCore import Qt, QTimer, QPropertyAnimation, QEasingCurve, pyqtProperty
from PyQt5.QtGui import QFont, QColor

MAX_ATTEMPTS = 3
PASSWORD = "root"  # You can change this

class AnimatedLabel(QLabel):
    """Futuristic animated label with glow effects"""
    def __init__(self, text="", parent=None):
        super().__init__(text, parent)
        self._glow_alpha = 0
        self.animation = QPropertyAnimation(self, b"glow_alpha")
        self.animation.setDuration(1000)
        self.animation.setEasingCurve(QEasingCurve.InOutQuad)
        
    @pyqtProperty(int)
    def glow_alpha(self):
        return self._glow_alpha
    
    @glow_alpha.setter
    def glow_alpha(self, alpha):
        self._glow_alpha = alpha
        self.update()
    
    def start_glow_animation(self):
        """Start pulsing glow animation"""
        self.animation.setStartValue(0)
        self.animation.setEndValue(255)
        self.animation.setLoopCount(-1)  # Infinite loop
        self.animation.start()
    
    def stop_glow_animation(self):
        """Stop glow animation"""
        self.animation.stop()
        self._glow_alpha = 0
        self.update()

class AboutDialog(QDialog):
    """Futuristic About dialog with developer information"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("About AI Login Gate")
        self.setFixedSize(500, 400)
        self.setWindowFlag(Qt.WindowStaysOnTopHint)
        
        # Futuristic styling
        self.setStyleSheet("""
            QDialog {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, 
                    stop:0 #0a0a0a, stop:0.5 #1a1a2e, stop:1 #16213e);
                border: 2px solid #00d4ff;
                border-radius: 15px;
            }
            QLabel {
                color: #00d4ff;
                background: transparent;
            }
            QTextBrowser {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, 
                    stop:0 rgba(10, 20, 40, 150), 
                    stop:0.5 rgba(20, 30, 60, 150), 
                    stop:1 rgba(30, 40, 80, 150));
                border: 1px solid #00d4ff;
                border-radius: 10px;
                color: #00ff88;
                font-family: 'Courier New', monospace;
                font-size: 12px;
                padding: 10px;
            }
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                    stop:0 #1e1e3f, stop:1 #2a2a5a);
                color: #00d4ff;
                border: 2px solid #00d4ff;
                border-radius: 10px;
                padding: 8px 15px;
                font-size: 12px;
                font-weight: bold;
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                    stop:0 #2a2a5a, stop:1 #1e1e3f);
                border: 2px solid #00ff88;
            }
            QPushButton:pressed {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                    stop:0 #3a3a6a, stop:1 #2e2e4f);
            }
        """)
        
        # Create layout
        layout = QVBoxLayout()
        
        # Title
        title = QLabel("🤖  Login Gate System 🤖")
        title.setFont(QFont("Orbitron", 16, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("""
            QLabel {
                color: #00ff88;
                font-size: 18px;
                font-weight: bold;
                margin: 10px;
                padding: 10px;
                border-bottom: 2px solid #00d4ff;
            }
        """)
        layout.addWidget(title)
        
        # Info text area
        info_text = QTextBrowser()
        info_text.setHtml("""
        <div style="text-align: center;">
            <h3 style="color: #00d4ff; margin-bottom: 15px;">🛡️ Quantum Security System 🛡️</h3>
            
            <p style="color: #00ff88; font-size: 14px; margin: 10px 0;">
                <strong>Developer:</strong> Aditya Deep Ratnam Singh<br>
                <strong>Version:</strong> 0.0.1<br>
                <strong>Date:</strong> July 20, 2025<br>
                <strong>Technology:</strong> PyQt5 + Python
            </p>
            
            <hr style="border: 1px solid #00d4ff; margin: 15px 0;">
            
            <h4 style="color: #00d4ff;">Features:</h4>
            <ul style="color: #00ff88; text-align: left; margin: 10px 20px;">
                <li>🚀 Futuristic ASCII Art Interface</li>
                <li>🔐 Quantum-Inspired Security Authentication</li>
                <li>🎨 Dynamic Gradient Backgrounds</li>
                <li>🔊 Text-to-Speech Voice Feedback</li>
                <li>⚡ Real-time Animation System</li>
                <li>🛡️ Multi-layered Security Protocol</li>
            </ul>
            
            <hr style="border: 1px solid #00d4ff; margin: 15px 0;">
            
            <p style="color: #00d4ff; font-style: italic; margin: 15px 0;">
                "Protecting Digital Frontiers with Style"
            </p>
            
            <p style="color: #ff6b6b; font-size: 12px; margin-top: 20px;">
                ⚠️ For authorized personnel only ⚠️
            </p>
        </div>
        """)
        info_text.setMaximumHeight(280)
        layout.addWidget(info_text)
        
        # Close button
        close_button = QPushButton("🔒 CLOSE")
        close_button.setFont(QFont("Courier New", 10, QFont.Bold))
        close_button.clicked.connect(self.accept)
        close_button.setFixedHeight(35)
        layout.addWidget(close_button)
        
        self.setLayout(layout)
        
        # Add glow effect to dialog
        glow = QGraphicsDropShadowEffect()
        glow.setBlurRadius(30)
        glow.setColor(QColor(0, 212, 255, 100))
        glow.setOffset(0, 0)
        self.setGraphicsEffect(glow)

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.attempts = 0
        self.setWindowTitle("|| ॐ श्री गणेशाय नमः ||")
        
        # Set fixed window size - cannot be resized or maximized
        self.setFixedSize(1400, 800)
        self.setGeometry(100, 100, 1400, 800)
        
        # Futuristic dark background with gradient
        self.setStyleSheet("""
            QWidget {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, 
                    stop:0 #0a0a0a, stop:0.5 #1a1a2e, stop:1 #16213e);
                color: #00d4ff;
            }
        """)

        # ASCII Art Display Widget
        self.ascii_display = QTextEdit(self)
        self.ascii_display.setReadOnly(True)
        self.ascii_display.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.ascii_display.setMinimumSize(800, 500)  # Much larger minimum size
        self.ascii_display.setMaximumSize(16777215, 16777215)
        self.ascii_display.setStyleSheet("""
            QTextEdit {
                border: 3px solid #00d4ff;
                border-radius: 20px;
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, 
                    stop:0 #000000, stop:0.3 #001122, stop:0.7 #001144, stop:1 #000000);
                color: #00ff88;
                margin: 5px;
                font-family: 'Courier New', 'Monaco', 'Lucida Console', monospace;
                font-size: 16px;
                font-weight: bold;
                padding: 15px;
                line-height: 1.2;
            }
        """)
        
        # Add enhanced glow effect to ASCII display
        ascii_glow = QGraphicsDropShadowEffect()
        ascii_glow.setBlurRadius(50)
        ascii_glow.setColor(QColor(0, 212, 255, 150))
        ascii_glow.setOffset(0, 0)
        self.ascii_display.setGraphicsEffect(ascii_glow)
        
        # Animation timers for ASCII art
        self.ascii_animation_timer = QTimer()
        self.ascii_animation_timer.timeout.connect(self.update_ascii_animation)
        self.ascii_frame = 0
        self.current_ascii_state = "idle"

        # Futuristic Password field
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setFont(QFont('Courier New', 24, QFont.Bold))  # Increased font size for bigger dots
        
        # Set fixed size for the password field
        self.password_input.setFixedSize(400, 60)  # Reduced to fit properly in container
        self.password_input.setMinimumSize(400, 60)
        self.password_input.setMaximumSize(400, 60)
        
        # Futuristic styling with animations
        self.password_input.setStyleSheet("""
            QLineEdit {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                    stop:0 #1e1e3f, stop:1 #2a2a5a);
                color: #00ff88;
                border: 2px solid #00d4ff;
                border-radius: 15px;
                padding: 15px;
                font-size: 24px;
                font-weight: bold;
                min-width: 400px;
                max-width: 400px;
                min-height: 60px;
                max-height: 60px;
                lineedit-password-character: 9679;
            }
            QLineEdit:focus {
                border: 2px solid #00ff88;
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                    stop:0 #2a2a5a, stop:1 #1e1e3f);
            }
            QLineEdit:hover {
                border: 2px solid #ff6b6b;
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                    stop:0 #3a1e3f, stop:1 #4a2a5a);
            }
        """)
        self.password_input.returnPressed.connect(self.check_password)
        
        # Add glow effect to password field
        password_glow = QGraphicsDropShadowEffect()
        password_glow.setBlurRadius(25)
        password_glow.setColor(QColor(0, 212, 255, 150))
        password_glow.setOffset(0, 0)
        self.password_input.setGraphicsEffect(password_glow)

        # Futuristic animated Info Label
        self.label = AnimatedLabel("ENTER PASSWORD")
        self.label.setFont(QFont("Orbitron", 20, QFont.Bold))  # Fallback to system font if Orbitron not available
        self.label.setStyleSheet("""
            QLabel {
                color: #00d4ff;
                background: transparent;
                padding: 15px;
                border: 2px solid transparent;
                border-radius: 10px;
                font-size: 20px;
                font-weight: bold;
                text-align: center;
            }
        """)
        self.label.setAlignment(Qt.AlignCenter)
        
        # Add glow effect to label
        label_glow = QGraphicsDropShadowEffect()
        label_glow.setBlurRadius(20)
        label_glow.setColor(QColor(0, 212, 255, 200))
        label_glow.setOffset(0, 0)
        self.label.setGraphicsEffect(label_glow)
        
        # Start pulsing animation for the label
        self.label.start_glow_animation()
        
        # Futuristic status bar
        self.status_bar = QLabel("SYSTEM READY • AWAITING AUTHENTICATION")
        self.status_bar.setFont(QFont("Courier New", 12, QFont.Bold))
        self.status_bar.setStyleSheet("""
            QLabel {
                color: #00d4ff;
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
                    stop:0 rgba(0, 212, 255, 30), stop:0.5 rgba(0, 212, 255, 10), stop:1 rgba(0, 212, 255, 30));
                padding: 8px;
                border-top: 1px solid #00d4ff;
                font-size: 12px;
                font-weight: bold;
            }
        """)
        self.status_bar.setAlignment(Qt.AlignCenter)

        # Futuristic Layouts
        input_layout = QVBoxLayout()
        input_layout.addWidget(self.label)
        input_layout.addSpacing(20)  # More space for futuristic look
        input_layout.addWidget(self.password_input)
        input_layout.addSpacing(30)
        input_layout.setAlignment(Qt.AlignCenter)
        
        # Create a futuristic container with border and glow
        input_container = QWidget()
        input_container.setFixedWidth(500)  # Reduced to give more space to ASCII art
        input_container.setStyleSheet("""
            QWidget {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, 
                    stop:0 rgba(10, 20, 40, 150), 
                    stop:0.5 rgba(20, 30, 60, 150), 
                    stop:1 rgba(30, 40, 80, 150));
                border: 2px solid #00d4ff;
                border-radius: 20px;
                margin: 15px;
            }
        """)
        input_container.setLayout(input_layout)
        
        # Add glow effect to container
        container_glow = QGraphicsDropShadowEffect()
        container_glow.setBlurRadius(40)
        container_glow.setColor(QColor(0, 212, 255, 80))
        container_glow.setOffset(0, 0)
        input_container.setGraphicsEffect(container_glow)

        main_layout = QHBoxLayout()
        main_layout.addWidget(input_container, 0)  # Fixed size for input container
        main_layout.addSpacing(15)  # Reduced spacing
        main_layout.addWidget(self.ascii_display, 4)  # More space for ASCII display
        main_layout.setContentsMargins(10, 10, 10, 10)  # Reduced margins for more space
        main_layout.setSpacing(15)  # Reduced spacing

        # Create futuristic title bar with About button
        title_bar = QHBoxLayout()
        
        # App title
        app_title = QLabel("🤖 AI LOGIN GATE SYSTEM 🤖")
        app_title.setFont(QFont("Orbitron", 14, QFont.Bold))
        app_title.setStyleSheet("""
            QLabel {
                color: #00d4ff;
                background: transparent;
                font-size: 14px;
                font-weight: bold;
                padding: 8px 15px;
            }
        """)
        
        # About button
        self.about_button = QPushButton("ℹ️ ABOUT")
        self.about_button.setFont(QFont("Courier New", 10, QFont.Bold))
        self.about_button.setFixedSize(100, 30)
        self.about_button.setStyleSheet("""
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                    stop:0 #1e1e3f, stop:1 #2a2a5a);
                color: #00d4ff;
                border: 2px solid #00d4ff;
                border-radius: 15px;
                padding: 5px 10px;
                font-size: 10px;
                font-weight: bold;
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                    stop:0 #2a2a5a, stop:1 #1e1e3f);
                border: 2px solid #00ff88;
                color: #00ff88;
            }
            QPushButton:pressed {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                    stop:0 #3a3a6a, stop:1 #2e2e4f);
            }
        """)
        self.about_button.clicked.connect(self.show_about_dialog)
        
        # Add glow effect to about button
        about_glow = QGraphicsDropShadowEffect()
        about_glow.setBlurRadius(15)
        about_glow.setColor(QColor(0, 212, 255, 100))
        about_glow.setOffset(0, 0)
        self.about_button.setGraphicsEffect(about_glow)
        
        title_bar.addWidget(app_title)
        title_bar.addStretch()  # Push about button to the right
        title_bar.addWidget(self.about_button)
        title_bar.setContentsMargins(15, 5, 15, 5)

        # Create the main layout with title bar and status bar
        main_with_status = QVBoxLayout()
        main_with_status.addLayout(title_bar)  # Add title bar at top
        main_with_status.addLayout(main_layout)
        main_with_status.addWidget(self.status_bar)
        main_with_status.setContentsMargins(0, 0, 0, 0)
        
        self.setLayout(main_with_status)

        # Start ASCII art animation
        self.show_ascii_art("idle")
        # Delay the welcome message to ensure display starts properly
        QTimer.singleShot(1000, lambda: self.speak("Welcome. Please enter your password."))
        self.password_input.setFocus()
    
    def get_ascii_art(self, art_type, frame=0):
        """Get ASCII art for different states and animation frames"""
        if art_type == "idle":
            idle_frames = [
                """
╔═══════════════════════════════════════════════════════════════════════════════╗
║                          🔐 QUANTUM SECURITY SYSTEM 🔐                        ║
║                              INITIALIZATION COMPLETE                          ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║                    ⚡⚡⚡ WAITING FOR AUTHENTICATION ⚡⚡⚡                    ║
║                                                                               ║
║                        ████ NEURAL SCANNER ACTIVE ████                       ║
║                                                                               ║
║            ┌─────────────────────────────────────────────────────┐            ║
║            │  ●●●●●●●●●●  [ SCANNING BIOMETRICS ]  ●●●●●●●●●●  │            ║
║            │                                                     │            ║
║            │     ████    ████    ████    ████    ████    ████    │            ║
║            │     ████    ████    ████    ████    ████    ████    │            ║
║            │     ████    ████    ████    ████    ████    ████    │            ║
║            │                                                     │            ║
║            │  ◆◆◆◆◆◆◆◆◆◆  [ QUANTUM ENCRYPTION ]  ◆◆◆◆◆◆◆◆◆◆  │            ║
║            └─────────────────────────────────────────────────────┘            ║
║                                                                               ║
║                         🛡️ SECURE LOGIN GATE ACTIVE 🛡️                        ║
║                                                                               ║
║                    STATUS: READY • PROTOCOLS: ENABLED                        ║
╚═══════════════════════════════════════════════════════════════════════════════╝
                """,
                """
╔═══════════════════════════════════════════════════════════════════════════════╗
║                          🔐 QUANTUM SECURITY SYSTEM 🔐                        ║
║                              INITIALIZATION COMPLETE                          ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║                    ⚡⚡⚡ WAITING FOR AUTHENTICATION ⚡⚡⚡                    ║
║                                                                               ║
║                        ████ NEURAL SCANNER ACTIVE ████                       ║
║                                                                               ║
║            ┌─────────────────────────────────────────────────────┐            ║
║            │  ██████████  [   SYSTEM READY   ]  ██████████  │            ║
║            │                                                     │            ║
║            │     ▓▓▓▓    ▓▓▓▓    ▓▓▓▓    ▓▓▓▓    ▓▓▓▓    ▓▓▓▓    │            ║
║            │     ▓▓▓▓    ▓▓▓▓    ▓▓▓▓    ▓▓▓▓    ▓▓▓▓    ▓▓▓▓    │            ║
║            │     ▓▓▓▓    ▓▓▓▓    ▓▓▓▓    ▓▓▓▓    ▓▓▓▓    ▓▓▓▓    │            ║
║            │                                                     │            ║
║            │  ◇◇◇◇◇◇◇◇◇◇  [ QUANTUM ENCRYPTION ]  ◇◇◇◇◇◇◇◇◇◇  │            ║
║            └─────────────────────────────────────────────────────┘            ║
║                                                                               ║
║                         🛡️ SECURE LOGIN GATE ACTIVE 🛡️                        ║
║                                                                               ║
║                    STATUS: STANDBY • PROTOCOLS: ENABLED                      ║
╚═══════════════════════════════════════════════════════════════════════════════╝
                """
            ]
            return idle_frames[frame % len(idle_frames)]
        
        elif art_type == "success":
            return """
╔═══════════════════════════════════════════════════════════════════════════════╗
║                          🔓 QUANTUM SECURITY SYSTEM 🔓                        ║
║                               ✅ ACCESS GRANTED ✅                            ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║                          🎉🎉🎉 SUCCESS! 🎉🎉🎉                            ║
║                                                                               ║
║                    ████████ AUTHENTICATION VERIFIED ████████                 ║
║                                                                               ║
║            ┌─────────────────────────────────────────────────────┐            ║
║            │  ████████████  [  WELCOME AUTHORIZED USER  ]  ████████████  │    ║
║            │                                                     │            ║
║            │     █████   █████   █████   █████   █████   █████   │            ║
║            │     █████   █████   █████   █████   █████   █████   │            ║
║            │     █████   █████   █████   █████   █████   █████   │            ║
║            │     █████   █████   █████   █████   █████   █████   │            ║
║            │     █████   █████   █████   █████   █████   █████   │            ║
║            │                                                     │            ║
║            │  ██████████████  [ SECURITY CLEARED ]  ██████████████  │        ║
║            └─────────────────────────────────────────────────────┘            ║
║                                                                               ║
║                        🌟 WELCOME TO THE SECURE ZONE 🌟                      ║
║                                                                               ║
║                 STATUS: AUTHORIZED • ACCESS: GRANTED • LEVEL: ADMIN          ║
╚═══════════════════════════════════════════════════════════════════════════════╝
            """
        
        elif art_type == "denied":
            return """
╔═══════════════════════════════════════════════════════════════════════════════╗
║                          🚫 QUANTUM SECURITY SYSTEM 🚫                        ║
║                               ❌ ACCESS DENIED ❌                             ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║                          🚨🚨🚨 INTRUDER ALERT! 🚨🚨🚨                      ║
║                                                                               ║
║                    ▓▓▓▓▓▓▓▓ UNAUTHORIZED ACCESS ▓▓▓▓▓▓▓▓                     ║
║                                                                               ║
║            ┌─────────────────────────────────────────────────────┐            ║
║            │  XXXXXXXXXXXX  [  SECURITY BREACH  ]  XXXXXXXXXXXX  │            ║
║            │                                                     │            ║
║            │     ▓▓▓▓▓   ▓▓▓▓▓   ▓▓▓▓▓   ▓▓▓▓▓   ▓▓▓▓▓   ▓▓▓▓▓   │            ║
║            │     ▓▓▓▓▓   ▓▓▓▓▓   ▓▓▓▓▓   ▓▓▓▓▓   ▓▓▓▓▓   ▓▓▓▓▓   │            ║
║            │     ▓▓▓▓▓   ▓▓▓▓▓   ▓▓▓▓▓   ▓▓▓▓▓   ▓▓▓▓▓   ▓▓▓▓▓   │            ║
║            │     ▓▓▓▓▓   ▓▓▓▓▓   ▓▓▓▓▓   ▓▓▓▓▓   ▓▓▓▓▓   ▓▓▓▓▓   │            ║
║            │     ▓▓▓▓▓   ▓▓▓▓▓   ▓▓▓▓▓   ▓▓▓▓▓   ▓▓▓▓▓   ▓▓▓▓▓   │            ║
║            │                                                     │            ║
║            │  ⚠️⚠️⚠️⚠️⚠️  [ LOCKDOWN INITIATED ]  ⚠️⚠️⚠️⚠️⚠️  │            ║
║            └─────────────────────────────────────────────────────┘            ║
║                                                                               ║
║                        🛡️ SYSTEM SECURITY COMPROMISED 🛡️                     ║
║                                                                               ║
║               STATUS: LOCKED • ACCESS: FORBIDDEN • ALERT: MAXIMUM            ║
╚═══════════════════════════════════════════════════════════════════════════════╝
            """
        
        return ""
    
    def show_ascii_art(self, art_type="idle"):
        """Display ASCII art in the text widget"""
        self.current_ascii_state = art_type
        if art_type == "idle":
            # Start animation for idle state
            self.ascii_frame = 0
            self.ascii_animation_timer.start(1000)  # Update every second
        else:
            # Stop animation for static states
            self.ascii_animation_timer.stop()
            
        # Set different colors for different states
        if art_type == "success":
            color = "#00ff88"
        elif art_type == "denied":
            color = "#ff4444"
        else:
            color = "#00ff88"
            
        # Create dynamic gradient background based on state
        if art_type == "success":
            bg_gradient = "stop:0 #001100, stop:0.3 #003300, stop:0.7 #002200, stop:1 #001100"
            border_color = "#00ff88"
        elif art_type == "denied":
            bg_gradient = "stop:0 #110000, stop:0.3 #330000, stop:0.7 #220000, stop:1 #110000"
            border_color = "#ff4444"
        else:
            bg_gradient = "stop:0 #000000, stop:0.3 #001122, stop:0.7 #001144, stop:1 #000000"
            border_color = "#00d4ff"
            
        self.ascii_display.setStyleSheet(f"""
            QTextEdit {{
                border: 3px solid {border_color};
                border-radius: 20px;
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, 
                    {bg_gradient});
                color: {color};
                margin: 5px;
                font-family: 'Courier New', 'Monaco', 'Lucida Console', monospace;
                font-size: 16px;
                font-weight: bold;
                padding: 15px;
                line-height: 1.2;
            }}
        """)
        
        art_text = self.get_ascii_art(art_type, self.ascii_frame)
        self.ascii_display.setText(art_text)
    
    def update_ascii_animation(self):
        """Update ASCII animation frame"""
        if self.current_ascii_state == "idle":
            self.ascii_frame += 1
            art_text = self.get_ascii_art("idle", self.ascii_frame)
            self.ascii_display.setText(art_text)

    def show_about_dialog(self):
        """Show the About dialog with developer information"""
        about_dialog = AboutDialog(self)
        about_dialog.exec_()

    def speak(self, text):
        try:
            # Create a new engine instance each time to avoid conflicts
            engine = pyttsx3.init()
            
            # Improved voice settings for clarity
            engine.setProperty('rate', 120)  # Slightly slower for better clarity
            engine.setProperty('volume', 1.0)  # Maximum volume
            
            # Get available voices and prefer clear English voices
            voices = engine.getProperty('voices')
            if voices:
                # Preferred voices in order of clarity
                preferred_voice_ids = [
                    'gmw/en-gb-x-rp',      # English (Received Pronunciation) - clearest
                    'gmw/en-us',           # English (America)
                    'gmw/en',              # English (Great Britain)
                    'gmw/en-gb-scotland'   # English (Scotland)
                ]
                
                selected_voice = None
                # Try to find preferred voice
                for pref_id in preferred_voice_ids:
                    for voice in voices:
                        if voice.id == pref_id:
                            selected_voice = voice
                            break
                    if selected_voice:
                        break
                
                # If no preferred voice found, use first available
                if selected_voice:
                    engine.setProperty('voice', selected_voice.id)
                    print(f"TTS Speaking: {text} (Using voice: {selected_voice.name})")
                else:
                    engine.setProperty('voice', voices[0].id)
                    print(f"TTS Speaking: {text} (Using default voice: {voices[0].name})")
            
            engine.say(text)
            engine.runAndWait()
            
            # Properly stop and delete the engine
            engine.stop()
            del engine
            
        except Exception as e:
            print(f"TTS Error: {e}")
            # Fallback: just print the message if TTS fails
            print(f"TTS Fallback: {text}")

    def cleanup_resources(self):
        """Clean up resources"""
        try:
            if hasattr(self, 'ascii_animation_timer'):
                self.ascii_animation_timer.stop()
        except Exception as e:
            print(f"Error cleaning up resources: {e}")
    
    def closeEvent(self, event):
        """Handle window close event with proper cleanup"""
        self.cleanup_resources()
        event.accept()

    def reset_password_field(self):
        """Reset the password field and ensure it's ready for input"""
        self.password_input.clear()
        self.password_input.setFocus()
        self.password_input.setEnabled(True)
        # Reset the label text if needed
        if self.attempts < MAX_ATTEMPTS:
            self.label.setText("ENTER PASSWORD")
            self.label.setStyleSheet("""
                QLabel {
                    color: #00d4ff;
                    background: transparent;
                    padding: 15px;
                    border: 2px solid transparent;
                    border-radius: 10px;
                    font-size: 20px;
                    font-weight: bold;
                    text-align: center;
                }
            """)
            # Reset status bar
            self.status_bar.setText("SYSTEM READY • AWAITING AUTHENTICATION")
            self.status_bar.setStyleSheet("""
                QLabel {
                    color: #00d4ff;
                    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
                        stop:0 rgba(0, 212, 255, 30), stop:0.5 rgba(0, 212, 255, 10), stop:1 rgba(0, 212, 255, 30));
                    padding: 8px;
                    border-top: 1px solid #00d4ff;
                    font-size: 12px;
                    font-weight: bold;
                }
            """)
        # Add a futuristic visual cue that the field is ready - pulsing green
        self.password_input.setStyleSheet("""
            QLineEdit {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                    stop:0 #1e3f1e, stop:1 #2a5a2a);
                color: #00ff88;
                border: 2px solid #00ff88;
                border-radius: 15px;
                padding: 15px;
                font-size: 24px;
                font-weight: bold;
                min-width: 400px;
                max-width: 400px;
                min-height: 60px;
                max-height: 60px;
            }
        """)
        # Reset border color back to normal after a short time
        QTimer.singleShot(800, self.reset_password_field_style)

    def reset_password_field_style(self):
        """Reset the password field border to normal futuristic style"""
        self.password_input.setStyleSheet("""
            QLineEdit {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                    stop:0 #1e1e3f, stop:1 #2a2a5a);
                color: #00ff88;
                border: 2px solid #00d4ff;
                border-radius: 15px;
                padding: 15px;
                font-size: 24px;
                font-weight: bold;
                min-width: 400px;
                max-width: 400px;
                min-height: 60px;
                max-height: 60px;
            }
            QLineEdit:focus {
                border: 2px solid #00ff88;
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                    stop:0 #2a2a5a, stop:1 #1e1e3f);
            }
            QLineEdit:hover {
                border: 2px solid #ff6b6b;
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                    stop:0 #3a1e3f, stop:1 #4a2a5a);
            }
        """)

    def check_password(self):
        text = self.password_input.text()
        if text == PASSWORD:
            self.label.setText("ACCESS GRANTED")
            self.label.setStyleSheet("""
                QLabel {
                    color: #00ff88;
                    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, 
                        stop:0 rgba(0, 255, 136, 50), stop:1 rgba(0, 255, 136, 20));
                    padding: 15px;
                    border: 2px solid #00ff88;
                    border-radius: 10px;
                    font-size: 24px;
                    font-weight: bold;
                    text-align: center;
                }
            """)
            self.label.stop_glow_animation()
            self.show_ascii_art("success")
            # Speak immediately for faster response
            QTimer.singleShot(50, lambda: self.speak("Access granted. You can proceed"))
            # Exit after showing success
            QTimer.singleShot(5000, self.close)  # Exit after 5 seconds
            # Update status bar
            self.status_bar.setText("AUTHENTICATION SUCCESSFUL • WELCOME")
            self.status_bar.setStyleSheet("""
                QLabel {
                    color: #00ff88;
                    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
                        stop:0 rgba(0, 255, 136, 50), stop:0.5 rgba(0, 255, 136, 20), stop:1 rgba(0, 255, 136, 50));
                    padding: 8px;
                    border-top: 1px solid #00ff88;
                    font-size: 12px;
                    font-weight: bold;
                }
            """)
            # Exit after showing success
            QTimer.singleShot(5000, self.close)  # Exit after 5 seconds
            # Clear and disable password field on success with success styling
            self.password_input.clear()
            self.password_input.setEnabled(False)
            self.password_input.setStyleSheet("""
                QLineEdit {
                    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                        stop:0 #1e3f1e, stop:1 #2a5a2a);
                    color: #00ff88;
                    border: 2px solid #00ff88;
                    border-radius: 15px;
                    padding: 15px;
                    font-size: 24px;
                    font-weight: bold;
                }
            """)
        else:
            self.attempts += 1
            self.label.setText(f"ACCESS DENIED ({self.attempts}/{MAX_ATTEMPTS})")
            self.label.setStyleSheet("""
                QLabel {
                    color: #ff4444;
                    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, 
                        stop:0 rgba(255, 68, 68, 50), stop:1 rgba(255, 68, 68, 20));
                    padding: 15px;
                    border: 2px solid #ff4444;
                    border-radius: 10px;
                    font-size: 22px;
                    font-weight: bold;
                    text-align: center;
                }
            """)
            self.label.stop_glow_animation()
            
            if self.attempts >= MAX_ATTEMPTS:
                # Update status bar for final failure
                self.status_bar.setText("AUTHENTICATION FAILED • ACCESS DENIED • SYSTEM LOCKED")
                self.status_bar.setStyleSheet("""
                    QLabel {
                        color: #ff4444;
                        background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
                            stop:0 rgba(255, 68, 68, 50), stop:0.5 rgba(255, 68, 68, 20), stop:1 rgba(255, 68, 68, 50));
                        padding: 8px;
                        border-top: 1px solid #ff4444;
                        font-size: 12px;
                        font-weight: bold;
                    }
                """)
                # Show access denied animation only on the last attempt
                self.show_ascii_art("denied")
                # Speak immediately for faster response
                QTimer.singleShot(50, lambda: self.speak("Access denied. Maximum attempts exceeded. Exiting."))
                # Exit after showing denial
                QTimer.singleShot(5000, self.close)  # Exit after 5 seconds
                # Clear and disable password field on final failure with error styling
                self.password_input.clear()
                self.password_input.setEnabled(False)
                self.password_input.setStyleSheet("""
                    QLineEdit {
                        background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                            stop:0 #3f1e1e, stop:1 #5a2a2a);
                        color: #ff4444;
                        border: 2px solid #ff4444;
                        border-radius: 15px;
                        padding: 15px;
                        font-size: 24px;
                        font-weight: bold;
                    }
                """)
            else:
                # Update status bar for retry
                self.status_bar.setText(f"AUTHENTICATION FAILED • ATTEMPT {self.attempts}/{MAX_ATTEMPTS} • TRY AGAIN")
                self.status_bar.setStyleSheet("""
                    QLabel {
                        color: #ff6b6b;
                        background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
                            stop:0 rgba(255, 107, 107, 40), stop:0.5 rgba(255, 107, 107, 15), stop:1 rgba(255, 107, 107, 40));
                        padding: 8px;
                        border-top: 1px solid #ff6b6b;
                        font-size: 12px;
                        font-weight: bold;
                    }
                """)
                # For non-final attempts, just show text and speak
                # Speak immediately for faster response
                QTimer.singleShot(50, lambda: self.speak("Access denied. Try again."))
                # Return to idle animation after a short delay
                QTimer.singleShot(1200, lambda: self.show_ascii_art("idle"))
                # Reset the password field and ensure it has focus
                QTimer.singleShot(1500, self.reset_password_field)
        
        # Clear password field and set focus immediately for non-final attempts
        if self.attempts < MAX_ATTEMPTS:
            # Clear password field immediately for all cases
            self.password_input.clear()
            # Set focus immediately without delay
            self.password_input.setFocus()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())
