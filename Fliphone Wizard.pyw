import sys
import subprocess
import markdown2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QApplication, QCheckBox, QDialog, QGridLayout, QLabel, QListView, QMessageBox, QProgressDialog, QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.statusBar = QtWidgets.QStatusBar()
        self.setStatusBar(self.statusBar)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_status_bar)
        self.timer.start(1000)
        
        self.central_widget = QtWidgets.QWidget()
        self.setCentralWidget(self.central_widget)

        self.setWindowTitle("Fliphone Wizard By: FliphoneBochur (v1.0.1)")
        self.setWindowIcon(QtGui.QIcon("fliphonewizard.ico"))

        self.banner_label = QtWidgets.QLabel(self)
        banner_pixmap = QtGui.QPixmap("fwbanner.png")
        self.banner_label.setPixmap(banner_pixmap)
        self.banner_label.setScaledContents(False)
        self.banner_label.setAlignment(QtCore.Qt.AlignCenter)

        self.adb_setup_button = QtWidgets.QPushButton("How to Setup ADB")
        self.install_button = QtWidgets.QPushButton("Install Apps")
        self.uninstall_button = QtWidgets.QPushButton("Uninstall Apps")
        self.credits_button = QtWidgets.QPushButton("Credits")
        self.adb_setup_button.setEnabled(False)
        self.install_button.setEnabled(False)
        self.uninstall_button.setEnabled(False)
        self.adb_setup_button.clicked.connect(self.adb_setup)
        self.install_button.clicked.connect(self.install_apps)
        self.uninstall_button.clicked.connect(self.uninstall_apps)
        self.credits_button.clicked.connect(self.credits)

        self.dropdown_menu = QtWidgets.QComboBox()
        self.dropdown_menu.addItems(["Please Select Your Phone","LG Classic","LG Exalt","Kyocera Cadence / DuraXV","Kyocera DuraXV Extreme","Schok Flip / Classic Flip","Sonim XP3 / XP5","TCL Flip 2","Alcatel Go Flip V"])
        self.dropdown_menu.currentTextChanged.connect(self.update_text_box)

        self.text_box = QtWidgets.QPlainTextEdit()
        self.text_box.setReadOnly(True)
        self.text_box.setMinimumHeight(self.text_box.minimumHeight() + 90)

        layout = QtWidgets.QGridLayout(self.central_widget)
        layout.addWidget(self.banner_label, 0, 0, 1, 2)
        layout.addWidget(self.dropdown_menu, 1, 0, 1, 2)
        layout.addWidget(self.adb_setup_button, 2, 0, 1, 2)
        layout.addWidget(self.install_button, 3, 0)
        layout.addWidget(self.uninstall_button, 3, 1)
        layout.addWidget(self.credits_button, 4, 0, 1, 2)
        layout.addWidget(self.text_box, 5, 0, 1, 2)
        
        #self.dropdown_menu.setCurrentIndex(1)
        #QTimer.singleShot(0, self.uninstall_apps)
        #QTimer.singleShot(0, self.install_apps_main) #**FINISH CODING** Also, uncomment code on top
        QTimer.singleShot(0, self.credits)
        
    def adb_setup(self):
        phone = self.dropdown_menu.currentText()
        if phone == "LG Classic":
            text = "To set up ADB on your phone, follow these steps:\n\n1. On your phone, Dial ##228378 and press call\n2. Scroll Down to Developer Options -> USB Debugging -> Turn ON\n3. Plug your phone into your computer (make sure you're using a file-transfer-compatible cable.)\n4. Go to Notifications, -> USB Configuration -> Charge Only.\n5. When your phone prompts you, asking you to approve the computers RSA fingerprint, check off always trust this device, and click yes.\n\nCheck the Status Bar on bottom of the main window to see if you have sucessfully connected.\n\nIf you think any of this information is wrong, could be written better, or if you have a problem, feel free to contact me. (Contact information is on bottom of the credits.)"
        elif phone == "LG Exalt":
            text = "To set up ADB on your phone, follow these steps:\n\n1. On your phone, Dial ##7764726220 (PROGRAM220)\n2. Enter 000000 as the service code.\n3. Scroll Down to Developer Options -> USB Debugging -> Turn ON\n3. Plug your phone into your computer (make sure you're using a file-transfer-compatible cable.)\n4. Go to Notifications, -> USB Configuration -> Charge Only.\n5. When your phone prompts you, asking you to approve the computers RSA fingerprint, check off always trust this device, and click yes.\n\nCheck the Status Bar on bottom of the main window to see if you have sucessfully connected.\n\nIf you think any of this information is wrong, could be written better, or if you have a problem, feel free to contact me. (Contact information is on bottom of the credits.)"
        elif phone == "Sonim XP3 / XP5":
            text = "To set up ADB on your phone, follow these steps:\n\n1. On your phone, Dial *#*#2387#*#*\n2. Enable Developer Options -> Scroll Down to USB Debugging -> Turn ON\n3. Plug your phone into your computer\n4.When your phone prompts you, asking you to approve the computers RSA fingerprint, check off always trust this device, and click yes.\n\nCheck the Status Bar on bottom of the main window to see if you have sucessfully connected.\n\nIf you think any of this information is wrong, could be written better, or if you have a problem, feel free to contact me. (Contact information is on bottom of the credits.)"
        elif phone == "TCL Flip 2" or phone == "Alcatel Go Flip V":
            text = "To set up ADB on your phone, follow these steps:\n\n1. On your phone, Dial *#*#33284#*#* (DEBUG) and click Yes\n2. Plug your phone into your computer\n3. When your phone prompts you, asking you to approve the computers RSA fingerprint, check off always trust this device, and click yes.\n\nCheck the Status Bar on bottom of the main window to see if you have sucessfully connected.\n\nIf you think any of this information is wrong, could be written better, or if you have a problem, feel free to contact me. (Contact information is on bottom of the credits.)"
        else:
            text = "To set up ADB on your phone, follow these steps:\n\n1. On your phone, go to Settings -> About phone -> Software information & Tap Build number 7 times until it tells you that you are a developer.\n2. Go back to the main settings menu -> Developer options -> USB Debugging -> Turn ON\n3. Plug your phone into your computer\n4. When your phone prompts you asking you to approve the computers RSA fingerprint, check off always trust this device, and click yes.\n\nCheck the Status Bar on bottom of the main window to see if you have sucessfully connected.\n\nIf you're still not connected, go to Notifications, -> USB Configuration -> Charge Only.\n\nIf you think any of this information is wrong, could be written better, or if you have a problem, feel free to contact me. (Contact information is on bottom of the credits.)"
        
        self.adb_setup_window = QtWidgets.QDialog(self, Qt.WindowCloseButtonHint)
        self.adb_setup_window.setWindowTitle("ADB Setup Wizard")
        self.adb_setup_window.setFixedSize(572, 500)
        
        text_edit = QtWidgets.QTextEdit(self.adb_setup_window)
        text_edit.setReadOnly(True)
        text_edit.setPlainText(text)
        font = QtGui.QFont()
        font.setPointSize(13)
        text_edit.setFont(font)
        text_edit.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse | QtCore.Qt.TextSelectableByKeyboard)
        
        layout = QtWidgets.QVBoxLayout(self.adb_setup_window)
        layout.addWidget(text_edit)
        
        self.adb_setup_window.show()

    def install_apps(self):
        phone = self.dropdown_menu.currentText()
        if phone == "LG Classic":
            page_text = "This phone is not designed to handle additional apps. Apps4Flip has developed a custom app launcher that you can install below. You should be able to access the launcher from notifications.\nIf you have the launcher installed already, just click Skip."
            self.install_command = 'adb install -g -r -d "A4F LG Classic Launcher.apk"'
            self.launch_command = 'adb shell monkey -p com.android.cts.apps4fliplauncher -c android.intent.category.LAUNCHER 1'
            self.package_name = "com.android.cts.apps4fliplauncher"
            right_button_text = "Skip"

        elif phone == "LG Exalt":
            page_text = "This phone is not designed to handle additional apps. Apps4Flip has developed a custom app launcher that you can install below. You should be able to access the launcher from notifications.\nIf you have the launcher installed already, just click Skip."
            self.install_command = 'adb install -g -r -d "A4F LG Exalt and Kyocera Launcher.apk"'
            self.launch_command = 'adb shell monkey -p com.android.cts.launcher -c android.intent.category.LAUNCHER 1'
            self.package_name = "com.android.cts.launcher"
            right_button_text = "Skip"
            
        elif phone == "Kyocera Cadence / DuraXV":
            page_text = "These phones are not designed to handle additional apps. Apps4Flip has developed a custom app launcher that you can install below. You should be able to access the launcher from notifications.\nIf you have the launcher installed already, just click Skip."
            self.install_command = 'adb install -g -r -d "A4F LG Exalt and Kyocera Launcher.apk"'
            self.launch_command = 'adb shell monkey -p com.android.cts.launcher -c android.intent.category.LAUNCHER 1'
            self.package_name = "com.android.cts.launcher"
            right_button_text = "Skip"            

        elif phone == "Kyocera DuraXV Extreme":
        #Change to Simple App Launcher (for this phone)
            page_text = "This phone doesn’t require an app launcher to launch installed apps, because all installed apps will come up in business tools, but if you would like to install an app launcher, you can below. To access the launcher, you can either replace one of your home screen icons with it, or set a direction key or programmable key to access it. The launcher is called Apps."
            self.install_command = 'adb install -g -r -d AppLauncher.apk'
            self.launch_command = ''
            right_button_text = "Skip"

        elif phone == "Schok Flip / Classic Flip":
            page_text = "These phones don’t require an app launcher to launch installed apps, as the apps come up on the main home screen."
            right_button_text = "Next"
            
        elif phone == "Sonim XP3 / XP5":
            page_text = "These phones don’t require an app launcher to launch installed apps, as the apps come up in the applications menu"
            right_button_text = "Next"

        elif phone == "Alcatel Go Flip V":
            page_text = "This phone is not designed to handle additional apps. If you are installing a few apps, you could set the direction keys to access them. If you’re downloading a bunch of apps, you can install an app launcher below. You’ll have to set a direction key to access it. The launcher is called Apps.\nIf you have the launcher installed already, just click Skip."
            self.install_command = 'adb install -g -r -d AppLauncher.apk'
            self.launch_command = ''
            self.package_name = "com.android.cts.applauncher"
            right_button_text = "Skip"

        self.install_launcher_window = QDialog(self, Qt.WindowCloseButtonHint)
        self.install_launcher_window.setWindowTitle("Installing Apps Wizard")
        self.install_launcher_window.setFixedSize(572, 500)

        self.title_label = QLabel("<h1>Welcome to the Installing Apps Wizard!</h1>")
        self.spacing_text = QLabel("")
        self.spacing_text.setStyleSheet("font-size: 1px;")
        self.subtitle_label = QLabel("You can start by installing an app launcher below.\n")
        self.subtitle_label.setStyleSheet("font-size: 20px;")
        self.page_text_label = QLabel(page_text)
        self.page_text_label.setStyleSheet("font-size: 16px;")
        self.page_text_label.setWordWrap(True)
        self.spacer1 = QSpacerItem(20, 60, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.install_launcher_button = QPushButton("                  Install Launcher                ")
        if phone == "Schok Flip / Classic Flip" or phone == "Sonim XP3 / XP5":
            self.install_launcher_button.hide()
        self.spacer2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.right_button = QPushButton(right_button_text)

        layout = QVBoxLayout(self.install_launcher_window)
        layout.addWidget(self.title_label)
        layout.addWidget(self.spacing_text)
        layout.addWidget(self.subtitle_label)
        layout.addWidget(self.page_text_label)
        layout.addItem(self.spacer1)
        layout.addWidget(self.install_launcher_button, alignment=Qt.AlignCenter)
        layout.addItem(self.spacer2)
        layout.addWidget(self.right_button, alignment=Qt.AlignRight)
        
        self.install_launcher_button.clicked.connect(self.install_launcher)
        if self.right_button.text() == "Next" or phone == "Kyocera DuraXV Extreme":
            self.right_button.clicked.connect(self.install_apps_main)
        else:
            self.right_button.clicked.connect(self.check_launcher)
        
        self.install_launcher_window.show()
    
    def install_launcher(self):
        installing_launcher_loading = QProgressDialog("Installing Launcher...", None, 0, 0, self)
        installing_launcher_loading.setWindowModality(Qt.WindowModal)
        installing_launcher_loading.setWindowTitle("Please Wait")
        installing_launcher_loading.setFixedSize(250, 60)
        installing_launcher_loading.setWindowFlags(installing_launcher_loading.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        installing_launcher_loading.show()

        install_process = subprocess.Popen(self.install_command, shell=True)
        while install_process.poll() is None:
            QApplication.processEvents()

        if self.launch_command:
            launch_process = subprocess.Popen(self.launch_command, shell=True)
            while launch_process.poll() is None:
                QApplication.processEvents()

        installing_launcher_loading.close()
        self.right_button.setText("Next")
    
    def check_launcher(self):
        output = subprocess.check_output("adb shell pm list packages launcher", shell=True, text=True)

        if self.package_name in output:
            self.install_apps_main()
        else:
            response = QMessageBox.question(self, "Confirmation",
            "Are you sure you want to continue without installing the app launcher?",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if response == QMessageBox.Yes:
                self.install_apps_main()
            else:
                pass
                
    def install_apps_main(self):
        self.install_launcher_window.close()
        self.install_apps_window = QDialog(self, Qt.WindowCloseButtonHint)
        self.install_apps_window.setWindowTitle("Installing Apps Wizard")
        self.install_apps_window.setFixedSize(572, 500)
        
        self.install_apps_label = QLabel("You can install apps below. The apps will first download and then install, so bigger apps will take longer.\nYou could see app details for each selected app in the box below.")
        self.install_apps_label.setStyleSheet("font-size: 15px;")
        self.install_apps_label.setWordWrap(True)
        
        self.apps_checklist_view = QListView()
        self.apps_checklist_model = QStandardItemModel()
        self.apps_checklist_view.setModel(self.apps_checklist_model)
        options = ["","2048", "24Six", "Accessibility", "AirPods Battery Utility", "And Daven", "AnyDesk", "Apps4Flip Mouse", "Boldbeast - Phone Call Recorder", "Brochos", "Button Mapper", "CRC Kosher", "Crossy Road", "DPI Changer", "ES File Manager", "Flappy Bird", "Google Maps", "Hebrew Keyboard", "Jstream", "MyBoy - Game Boy Advance Emulator", "Screen Recorder", "Sefardi Siddur ", "Sefaria", "Smart Zmanim", "Smartlist - Jewish Phonebook", "SMS Backup & Restore", "Snake Game", "Stratego", "Teffilas Haderech", "Tehillim", "TorahAnytime Daily Dose", "TorahAnytime New App", "TorahAnytime Old App", "Uber", "Unit Converter", "Voice Access", "Waze", "Weather"]
        for option in options:
            if option:
                item = QStandardItem(option)
                item.setCheckable(True)
                self.apps_checklist_model.appendRow(item)
        self.apps_checklist_view.setCurrentIndex(self.apps_checklist_model.index(0,0))
        
        self.apps_text_box = QPlainTextEdit()
        self.apps_text_box.setTextInteractionFlags(Qt.NoTextInteraction | Qt.TextSelectableByMouse | Qt.TextSelectableByKeyboard)
        self.install_apps_button = QPushButton("                     Install                       ")
        self.cancel_button = QPushButton("Cancel")
        
        layout = QVBoxLayout(self.install_apps_window)
        layout.addWidget(self.install_apps_label)
        layout.addWidget(self.apps_checklist_view)
        layout.addWidget(self.apps_text_box)
        self.apps_text_box.setFixedHeight(80)
        layout.addWidget(self.install_apps_button, alignment=Qt.AlignCenter)
        layout.addWidget(self.cancel_button, alignment=Qt.AlignRight)
        
        self.apps_checklist_view.selectionModel().currentChanged.connect(self.update_apps_text_box)
        self.install_apps_button.clicked.connect(self.installing_apps)
        self.cancel_button.clicked.connect(lambda: self.install_apps_window.close())

        self.install_apps_window.show()
        
    def update_apps_text_box(self, current_index, previous_index):
        app = self.apps_checklist_model.data(current_index)
        if app == "2048":
            self.apps_text_box.setPlainText("The addictive 2048 game!")
        elif app == "24Six":
            self.apps_text_box.setPlainText("The Future of Jewish Music! \nNote that since this app is designed for smartphones, the screen might be too small for it. To get full functionality of the music player, and for the library to work, you'll have to lower the phone screen density to around 80. You can do this with the DPI Changer listed below. They are working on a version for flip phones that's coming soon!")
        elif app == "Accessibility":
            self.apps_text_box.setPlainText("If you want to use multiple apps that require accessibility services at once (AnyDesk, Mouse, Voice Control, Button Mapper), you could use this app to enable them simultaniously.")
        elif app == "AirPods Battery Utility":
            self.apps_text_box.setPlainText("AirBattery displays the battery life of you airpods every time you connect them to your phone.")
        elif app == "And Daven":
            self.apps_text_box.setPlainText("AndDaven is a complete Ahskenazi siddur with a stunning hebrew font.")
        elif app == "AnyDesk":
            self.apps_text_box.setPlainText("Remote desktop software on your phone. You can remote into a computer (controlling it doesn't work so well) from your phone, and you could remote from your computer into your phone! This app requires use of accessability services, so installing it will disable any other service you have running. You could have multiple services running at once with the Accessibility app.")
        elif app == "Apps4Flip Mouse":
            self.apps_text_box.setPlainText("Control apps with a mouse! Press * 3 times to enter or exit. I'd recommend disabling scroll mode (from in the app) because it doesn't work so well. Note that installing this app on an LG phone will automatically uninstall the built-in voice access. You can install a different version of voice accesss below.")
        elif app == "Boldbeast - Phone Call Recorder":
            self.apps_text_box.setPlainText("Boldbeast recorder is a simple, yet powerful app to record your phone calls. And it records both sides loud and clear. Just remember, in some states you must to ask permission to record someone. The recordings should save in internal storage.")
        elif app == "Brochos":
            self.apps_text_box.setPlainText("Brochos tells you the brochos for all kinds of food.")
        elif app == "Button Mapper":
            self.apps_text_box.setPlainText("Take control of your phone's buttons! With button mapper, you can choose what happens when you short press, long press, or double click any button on your phone. Perfect way to launch those apps that you need to access quickly!")
        elif app == "CRC Kosher":
            self.apps_text_box.setPlainText("Kashrus information on the go! CRC Kosher is an invaluable guide to figuring out what you can and can not eat. Features an up-to-date database on many items.")
        elif app == "Crossy Road":
            self.apps_text_box.setPlainText("Why did the chicken cross the road?\nTo play this adictive game!")
        elif app == "DPI Changer":
            self.apps_text_box.setPlainText("DPI stands for Dots per Inch (AKA Density). You could use this app to change phone screen density.  If you lower the density, you could fit more things on your screen. Certain Apps, (like 24Six) need the screen density to be lowered for full functionality.")
        elif app == "ES File Manager":
            self.apps_text_box.setPlainText("ES File Manager is the best file manager for android phones. Allowing you to copy files between sd cards and your flip phones storage, has a built-in music player, and many more features.")
        elif app == "Flappy Bird":
            self.apps_text_box.setPlainText("Make sure you don't break your phone when playing this game. What's the highest you could get?")
        elif app == "Google Maps":
            self.apps_text_box.setPlainText("Google Maps is a feature-packed navigation app, now available for your flip phone! With directions for Walking, biking, driving, and public transportation, this app is perfect for anyone.")
        elif app == "Hebrew Keyboard":
            self.apps_text_box.setPlainText("Hold down # to change langauges. If you're on a Kyocera or LG Phone, you'll have to configure the buttons differently, because # is space.")
        elif app == "Jstream":
            self.apps_text_box.setPlainText("Jstream allows you to stream your favorite jewish radio station.")
        elif app == "MyBoy - Game Boy Advance Emulator":
            self.apps_text_box.setPlainText("MyBoy is a Game Boy Advance emulator which allows you to play any game boy advance game on your flip phone. Yes that includes mario and all of those old classics of your childhood! MyBoy does not include any built in games, so in order to play games, you have to download roms and put them in your internal storage. Please note: By default the controls are not mapped correctly to a flip phone keypad. To map them properly, go to settings in the app and remap the controller keys to your personal preference.")
        elif app == "Screen Recorder":
            self.apps_text_box.setPlainText("Record videos of your screen! Needs a mouse to start. This app might not work on the Kyocera Cadence. The recordings should save in internal storage.")
        elif app == "Sefardi Siddur ":
            self.apps_text_box.setPlainText("Siddur Sefardi is a complete Sefardi siddur with a stunning hebrew font.")
        elif app == "Sefaria":
            self.apps_text_box.setPlainText("Sefaria delivers 3,000 years of Jewish texts (Torah, Tanach, Mishnah, Talmud, and more) to your phone. Search by keyword or browse the table of contents to explore texts, translations, and commentaries. Plus - the entire library can fit on your phone (500MB) so you can learn while you're offline.")
        elif app == "Smart Zmanim":
            self.apps_text_box.setPlainText("Smart Zmanim is clock full of useful features, including Zmanim alarms, notifications, hebrew date, and much much more!")
        elif app == "Smartlist - Jewish Phonebook":
            self.apps_text_box.setPlainText("Smartlist allows you to view phone numbers for any one jewish. Featuring updated databases of many jewish towns, smartlist is an essential app for the frum flip phone user.")
        elif app == "SMS Backup & Restore":
            self.apps_text_box.setPlainText("Useful app for backing up texts and call logs. You can set up a recurring backup to make sure your data is safe. (This app is recommended for the LG Classic which is known to randomly delete stuff. You'll have to set this app as your default messaging app to restore texts. If you want to text after that, you'll need to change the default app back. More details on that could be found here: https://forums.apps4flip.com/d/53/117")
        elif app == "Snake Game":
            self.apps_text_box.setPlainText("The classic snake game!")
        elif app == "Stratego":
            self.apps_text_box.setPlainText("Strategy is a clone of Stratego, Now available for flip phones! Enjoy hours of kosher fun playing this addictive and strategic game.")
        elif app == "Teffilas Haderech":
            self.apps_text_box.setPlainText("Teffilas haderech helps you to say teffilas haderech with utmost concentration while driving! It supports Hebrew, English, and Transliterated versions. Also includes a say-along audio so that you can keep you eyes on the road.")
        elif app == "Tehillim":
            self.apps_text_box.setPlainText("A complete tehillim for your flip phone. You may want to adjust the font size to mitigate the strain the small screen can cause to your eyes. You can do this by selecting Font from the menu after tapping the 3 dots in the corner, and then choosing a smaller size.")
        elif app == "TorahAnytime Daily Dose":
            self.apps_text_box.setPlainText("Short, Powerful, Life-Changing Clips from your Favorite TorahAnytime Speakers.")
        elif app == "TorahAnytime New App":
            self.apps_text_box.setPlainText("Watch, listen, and download your favorite classes and speakers on the world’s largest originally recorded Torah library. Over 1,100 different speakers with over 200,000 shiurim! The old app works better on flip phones, but this one has more features.")
        elif app == "TorahAnytime Old App":
            self.apps_text_box.setPlainText("Watch, listen, and download your favorite classes and speakers on the world’s largest originally recorded Torah library. Over 1,100 different speakers with over 200,000 shiurim! This app works better on flip phones than the new one, but has less features.")
        elif app == "Uber":
            self.apps_text_box.setPlainText("Uber for your flip phone. This is a modified uber app which includes a cursor to help you navigate the app. Please note you must create an uber account and set your payment method from another phone before signing into your account on your flip phone. Also, to place a ride, click on the “W” on the main menu, then use the saved destination feature to select your start and end locations.")
        elif app == "Unit Converter":
            self.apps_text_box.setPlainText("Convert from any measurement back and forth. Features inlclude Currency, Volume, Height, Weight, and many more measurements.")
        elif app == "Voice Access":
            self.apps_text_box.setPlainText("Voice access allows you to control your phone entirely with your voice, including apps that do not support a flip phone's keypad. If you want to get rid of the blue voice access button, you can tell Voice Access, ''open Voice Access settings,'' and switch it off from there. Note that installing this app on an LG phone will automatically uninstall the built-in voice access.")
        elif app == "Waze":
            self.apps_text_box.setPlainText("Waze works great on flip phones, just follow the directions in app to get started. Installing this app will also install the waze launcher which makes it easier to enter an address. Please Note: On a LG Classic, you should turn on the phone's location setting before installing the app.")
        elif app == "Weather":
            self.apps_text_box.setPlainText("Weather uses your gps location to give you the hour by hour forecast, as well as a 5 day forecast. It also supports multiple locations at once.")
            
    def installing_apps(self):
        pass
        
    def uninstall_apps(self):
        self.uninstall_apps_window = QDialog(self, Qt.WindowCloseButtonHint)
        self.uninstall_apps_window.setWindowTitle("Uninstalling Apps Wizard")
        self.uninstall_apps_window.setFixedSize(572, 500)
        
        self.uninstall_title_label = QLabel("<h1>Welcome to the Uninstalling Apps Wizard!</h1>")
        self.uninstall_apps_label = QLabel("You can uninstall built-in phone apps below. Uninstalling installed apps will be added in a later version. You can only get back these apps with a factory reset.")
        self.uninstall_apps_label.setStyleSheet("font-size: 15px;")
        self.uninstall_apps_label.setWordWrap(True)
        
        self.uninstall_checklist_view = QListView()
        self.uninstall_checklist_model = QStandardItemModel()
        self.uninstall_checklist_view.setModel(self.uninstall_checklist_model)
        phone = self.dropdown_menu.currentText()
        if phone == "LG Classic" or phone == "LG Exalt":
            options = ["Browser", "Email", "Texting", "FM Radio", "Video", "Camera"]
            self.browser_command = ['adb shell pm uninstall -k --user 0 com.android.browser', 'adb shell pm uninstall -k --user 0 com.android.quicksearchbox']
            self.email_command = ['adb shell pm uninstall -k --user 0 com.lge.email']
            self.texting_command = ['adb shell pm uninstall -k --user 0 com.android.mms', 'adb shell pm uninstall -k --user 0 com.verizon.messaging.vzmsgs']
            self.fm_radio_command = ['adb shell pm uninstall -k --user 0 com.lge.fmradio']
            self.video_command = ['adb shell pm uninstall -k --user 0 com.lge.videoplayer']
            self.camera_command = ['adb shell pm uninstall -k --user 0 com.lge.camera']
            self.restart_required = 'Yes'
        elif phone == "Kyocera Cadence / DuraXV":
            options = ["Browser", "Email", "Texting", "FM Radio", "Camera"]
            self.browser_command = ['adb shell pm uninstall -k --user 0 com.android.browser', 'adb shell pm disable-user --user 0 com.android.browser', 'adb shell pm uninstall -k --user 0 com.android.quicksearchbox']
            self.email_command = ['adb shell pm uninstall -k --user 0 com.android.email', 'adb shell pm disable-user --user 0 com.android.email']
            self.texting_command = ['adb shell pm uninstall -k --user 0 com.android.mms', 'adb shell pm uninstall -k --user 0 com.verizon.messaging.vzmsgs', 'adb shell pm disable-user -k --user 0 com.android.mms', 'adb shell pm disable-user -k --user 0 com.verizon.messaging.vzmsgs']
            self.fm_radio_command = ['adb shell pm uninstall -k --user 0 jp.kyocera.kc_fmradio']
            self.camera_command = ['adb shell pm uninstall -k --user 0 com.android.camera']
            self.restart_required = 'No'
        elif phone == "Kyocera DuraXV Extreme":
            options = ["Browser", "Email", "Texting", "FM Radio", "Camera"]
            self.browser_command = ['adb shell pm uninstall -k --user 0 com.android.browser', 'adb shell pm uninstall -k --user 0 com.android.quicksearchbox']
            self.email_command = ['adb shell pm uninstall -k --user 0 com.android.email']
            self.texting_command = ['adb shell pm uninstall -k --user 0 com.android.mms', 'adb shell pm uninstall -k --user 0 com.verizon.messaging.vzmsgs']
            self.fm_radio_command = ['adb shell pm uninstall -k --user 0 jp.kyocera.kc_fmradio']
            self.camera_command = ['adb shell pm uninstall -k --user 0 com.android.camera']
            self.restart_required = 'No'
        elif phone == "Schok Flip / Classic Flip":
            options = ["Browser", "Texting", "FM Radio", "Camera"]
            self.browser_command = ['adb shell pm uninstall -k --user 0 com.android.browser', 'adb shell pm uninstall -k --user 0 com.android.quicksearchbox', 'adb shell pm uninstall -k --user 0 com.android.vending']
            self.texting_command = ['adb shell pm uninstall -k --user 0 com.android.mms']
            self.fm_radio_command = ['adb shell pm uninstall -k --user 0 com.caf.fmradio', 'adb shell pm uninstall -k --user 0 com.umx.fmradio']
            self.camera_command = ['adb shell pm uninstall -k --user 0 com.android.camera']
            self.restart_required = 'No'
        elif phone == "Sonim XP3 / XP5":
            options = ["Browser", "Texting", "FM Radio", "Camera"]
            self.browser_command = ['adb shell pm uninstall -k --user 0 com.android.browser', 'adb shell pm uninstall -k --user 0 com.android.quicksearchbox', 'adb shell pm uninstall -k --user 0 com.android.vending']
            self.texting_command = ['adb shell pm uninstall -k --user 0 com.android.mms']
            self.fm_radio_command = ['adb shell pm uninstall -k --user 0 com.caf.fmradio']
            self.camera_command = ['adb shell pm uninstall -k --user 0 com.sonim.camera']
            self.restart_required = 'No'
        elif phone == "TCL Flip 2":
            options = ["Browser", "Email", "Texting", "Camera"]
            self.browser_command = ['adb shell pm disable-user --user 0 org.chromium.chrome', 'adb shell pm disable-user --user 0 com.android.quicksearchbox']
            self.email_command = ['adb shell pm disable-user --user 0 com.android.email']
            self.texting_command = ['adb shell pm disable-user --user 0 com.android.mms']
            self.camera_command = ['adb shell pm disable-user --user 0 com.tcl.camera']
            self.restart_required = 'Yes'
        elif phone == "Alcatel Go Flip V":
            options = ["Browser", "Email", "Texting", "Camera"]
            self.browser_command = ['adb shell pm disable-user --user 0 org.chromium.chrome', 'adb shell pm disable-user --user 0 com.android.quicksearchbox']
            self.email_command = ['adb shell pm disable-user --user 0 com.android.email']
            self.texting_command = ['adb shell pm disable-user --user 0 com.android.mms']
            self.camera_command = ['adb shell pm disable-user --user 0 com.android.camera2']
            self.restart_required = 'Yes'
        for option in options:
            if option:
                item = QStandardItem(option)
                item.setCheckable(True)
                self.uninstall_checklist_model.appendRow(item)
        
        self.uninstall_apps_button = QPushButton("                     Uninstall                       ")
        self.cancel_button = QPushButton("Cancel")
        
        layout = QVBoxLayout(self.uninstall_apps_window)
        layout.addWidget(self.uninstall_title_label)
        layout.addWidget(self.uninstall_apps_label)
        layout.addWidget(self.uninstall_checklist_view)
        layout.addWidget(self.uninstall_apps_button, alignment=Qt.AlignCenter)
        layout.addWidget(self.cancel_button, alignment=Qt.AlignRight)

        self.uninstall_apps_button.clicked.connect(self.uninstalling_apps)
        self.cancel_button.clicked.connect(lambda: self.uninstall_apps_window.close())
        
        self.uninstall_apps_window.show()
        
    def uninstalling_apps(self):
        selected_apps = []
        for row in range(self.uninstall_checklist_model.rowCount()):
            item = self.uninstall_checklist_model.item(row)
            if item.checkState() == Qt.Checked:
                selected_apps.append(item.text())

        if not selected_apps:
            QMessageBox.warning(self, "Error", "Please select at least one app to uninstall.")
            return

        phone = self.dropdown_menu.currentText()
        commands = []
        homescreen_app = 'No'

        for app in selected_apps:
                if app == "Browser":
                    commands.extend(self.browser_command)
                    homescreen_app = 'Yes'
                elif app == "Email":
                    commands.extend(self.email_command)
                    if phone == "LG Exalt" or phone == "Alcatel Go Flip V":
                        homescreen_app = 'Yes'
                elif app == "Texting":
                    commands.extend(self.texting_command)
                    homescreen_app = 'Yes'
                elif app == "FM Radio":
                    commands.extend(self.fm_radio_command)
                elif app == "Video":
                    commands.extend(self.video_command)
                elif app == "Camera":
                    commands.extend(self.camera_command)
                    if not phone == "Alcatel Go Flip V":
                        homescreen_app = 'Yes'
        
        uninstall_loading = QProgressDialog(self)
        uninstall_loading.setLabelText("Uninstalling apps...")
        uninstall_loading.setMinimum(0)
        uninstall_loading.setMaximum(len(commands))
        uninstall_loading.setCancelButton(None)
        uninstall_loading.setWindowModality(Qt.WindowModal)
        uninstall_loading.setWindowTitle("Please Wait")
        uninstall_loading.setFixedSize(250, 60)
        uninstall_loading.setWindowFlags(uninstall_loading.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        uninstall_loading.show()

        for i, command in enumerate(commands):
            subprocess.run(command, shell=True)
            uninstall_loading.setValue(i + 1)

        uninstall_loading.close()
        
    def uninstalling_apps(self):
        selected_apps = []
        for row in range(self.uninstall_checklist_model.rowCount()):
            item = self.uninstall_checklist_model.item(row)
            if item.checkState() == Qt.Checked:
                selected_apps.append(item.text())

        if not selected_apps:
            QMessageBox.warning(self, "Error", "Please select at least one app to uninstall.")
            return

        if "Browser" not in selected_apps:
            response = QMessageBox.question(self, "Confirmation", "Are you sure you want to continue without uninstalling the browser?", QMessageBox.Yes | QMessageBox.No)
            if response == QMessageBox.No:
                return

        phone = self.dropdown_menu.currentText()
        commands = []
        homescreen_app = 'No'

        for app in selected_apps:
            if app == "Browser":
                commands.extend(self.browser_command)
                homescreen_app = 'Yes'
            elif app == "Email":
                commands.extend(self.email_command)
                if phone == "LG Exalt" or phone == "Alcatel Go Flip V":
                    homescreen_app = 'Yes'
            elif app == "Texting":
                commands.extend(self.texting_command)
                homescreen_app = 'Yes'
            elif app == "FM Radio":
                commands.extend(self.fm_radio_command)
            elif app == "Video":
                commands.extend(self.video_command)
            elif app == "Camera":
                commands.extend(self.camera_command)
                if not phone == "Alcatel Go Flip V":
                    homescreen_app = 'Yes'

        uninstall_loading = QProgressDialog(self)
        uninstall_loading.setLabelText("Uninstalling apps...")
        uninstall_loading.setMinimum(0)
        uninstall_loading.setMaximum(len(commands))
        uninstall_loading.setCancelButton(None)
        uninstall_loading.setWindowModality(Qt.WindowModal)
        uninstall_loading.setWindowTitle("Please Wait")
        uninstall_loading.setFixedSize(250, 60)
        uninstall_loading.setWindowFlags(uninstall_loading.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        uninstall_loading.show()

        QApplication.processEvents()
        for i, command in enumerate(commands):
            if i < len(selected_apps):
                app_name = selected_apps[i]
                uninstall_loading.setLabelText(f"Uninstalling {app_name}...")
            else:
                app_name = ""
            subprocess.run(command, shell=True)
            uninstall_loading.setValue(i + 1)
            QApplication.processEvents()

        uninstall_loading.close()

        if self.restart_required == 'Yes' and homescreen_app == 'Yes':
            response = QMessageBox.question(self, "Restart Required", "A restart is required for app icons to disappear from your phone's homescreen. Would you like to restart now?", QMessageBox.Yes | QMessageBox.No)
            if response == QMessageBox.Yes:
                subprocess.run(['adb', 'reboot'], shell=True)
                self.uninstall_apps_window.close()
        else:
            QMessageBox.information(self, "Uninstallation Complete", "Apps uninstalled successfully!")
        self.cancel_button.setText("Close")

    def credits(self):
        self.credit_window = QtWidgets.QDialog(self, Qt.WindowCloseButtonHint)
        self.credit_window.setWindowTitle("Credits")
        self.credit_window.setFixedSize(572, 500)

        text_browser = QtWidgets.QTextBrowser(self.credit_window)
        text_browser.setReadOnly(True)
        with open("credits.md", "r") as f:
            text = f.read()
            html = markdown2.markdown(text)
            text_browser.setHtml(html)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(text_browser)
        self.credit_window.setLayout(layout)

        self.credit_window.exec_()

    def update_text_box(self, text):
        phone = self.dropdown_menu.currentText()
        if phone == "LG Classic":
            self.text_box.setPlainText("Model: L125DL\n\nThis phone is also known as the LG Wine 2")
        elif phone == "LG Exalt":
            self.text_box.setPlainText("Model: VN220 / UN220")
        elif phone == "Kyocera Cadence / DuraXV":
            self.text_box.setPlainText("The Kyocera DuraXV (E4610) is a rugged phone with a round-ish botton. The one with the square-ish bottom is the DuraXV Extreme")
        elif phone == "Kyocera DuraXV Extreme":
            self.text_box.setPlainText("This selection includes all rugged Kyocera models with a square-ish bottom. This includes the DuraXV Extreme (E4810), DuraXV Extreme+ (E4811), DuraXE Epic (E4710, E4830), and DuraXA Equip (E4510) models.")
        elif phone == "Schok Flip / Classic Flip":
            self.text_box.setPlainText("In addition to being able to uninstall the browser and other apps on these phones, you can use the Lock Control features in settings to block access to certain apps and block hotspot, data, factory reset, etc.")
        elif phone == "Sonim XP3 / XP5":
            self.text_box.setPlainText("This phone selection includes all variants of these models.\n\nFor more information on the XP3, see this post: https://forums.apps4flip.com/d/122. \n\nYou can kasher the Verizon version of the XP5 yourself for free (not just uninstalling the browser)! For information on that, see https://www.apps4flip.com/posts/sonimxp5/.")
        elif phone == "TCL Flip 2":
            self.text_box.setPlainText("Note: The naming for the Alcatel / TCL Flip phones can be very confusing. The selected phone refers only to TCL models which run Android. Those models are the 4058C, 4058C, 4058R, 4058L, 4058W, 4058E, T408DL, and T408DG. \nFor more information on this, see https://forums.apps4flip.com/d/832/2 \n\nYou can kasher this phone (the T408DL, 4058E, or 4058L models) yourself for free (not just uninstalling the apps)! For information on kosher ROMs, see https://www.apps4flip.com/posts/tclflip/ and  https://forums.apps4flip.com/d/693. \n\nApp Installation on this phone is not supported by defalt, but some users on the forum were able to hack it. For more information on that, and to see how you can install apps on this phone, see https://forums.apps4flip.com/d/596 and https://github.com/neutronscott/flip2/wiki.")
        elif phone == "Alcatel Go Flip V":
            self.text_box.setPlainText("Note: The naming for the Alcatel / TCL Go Flip phones can be very confusing. Most of the Alcatel Go Flips run KaiOS which this program doesn't support. Some people may say a phone is one thing, but they'll sell you something else. This phone selection refers only to the 4051S model which runs Android. \nFor more information, see https://forums.apps4flip.com/d/832/2")
        else:
             self.text_box.setPlainText("")
        self.text_box.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse | QtCore.Qt.TextSelectableByKeyboard)

    def update_status_bar(self):
        proc = subprocess.Popen("adb devices", stdout=subprocess.PIPE, shell=True)
        output, error = proc.communicate()

        if error:
            self.statusBar.showMessage("Error: " + error.decode())
            self.device_connected = False
            return
            
        lines = output.decode().split("\n")[1:-2]

        if len(lines) == 0:
            self.statusBar.showMessage("Status: Disconnected")
            self.device_connected = False
        elif len(lines) > 1:
            self.statusBar.showMessage("Error: More than one device")
            self.device_connected = False
        else:
            device, status = lines[0].split()
            if status == "unauthorized":
                self.statusBar.showMessage("Status: Unauthorized")
                self.device_connected = False
            elif status == "device":
                self.statusBar.showMessage("Status: Connected")
                self.device_connected = True
            else:
                self.statusBar.showMessage("Error: Unknown Status")
                self.device_connected = False

        self.install_button.setEnabled(self.device_connected)
        self.uninstall_button.setEnabled(self.device_connected)
        
        phone = self.dropdown_menu.currentText()
        if phone == "Please Select Your Phone":
            self.adb_setup_button.setEnabled(False)
            self.install_button.setEnabled(False)
            self.uninstall_button.setEnabled(False)
        elif phone == "TCL Flip 2":
            self.install_button.setEnabled(False)
            self.adb_setup_button.setEnabled(True)
        else:
            self.adb_setup_button.setEnabled(True)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
