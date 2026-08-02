# Changelog

All notable changes to AIOS will be documented in this file.

---
## Version 0.5.0 (In Progress)

### Added
- Application runtime using a `while` loop
- AIOS Main Menu
- Menu navigation system
- User choice handling
- Exit option controlled by application state (`logged_in`)

### Improved
- AIOS now remains active until the user chooses to exit.
- Introduced a clear separation between initialization and runtime.
- Established the foundation for a fully interactive command-line application.

### Upcoming
- Integrate Calculator into the Main Menu.
- Integrate Profile Viewer into the Main Menu.

## Version 0.4.0

### Added

- User role assignment system
- Multi-level verification using `if`, `elif`, and `else`
- AI-inspired user role classification
- Smarter personalized messages

### Improved

- Replaced multiple independent `if` statements with a single `if-elif-else` decision chain
- Improved profile display and verification flow
- Continued organizing AIOS into clear functional sections

---

## Version 0.3.0

### Added

- Personalized Messages section
- Adult user recognition
- Chelsea supporter recognition
- GitHub username recognition

### Improved

- Cleaner input handling using `.strip()`
- Automatic text formatting using `.title()` and `.lower()`
- Introduced a reusable separator variable for cleaner code

---

## Version 0.2.0

### Added

- Profile validation
- Adult verification
- Favourite club validation
- GitHub username validation

### Improved

- Better project structure
- Cleaner terminal interface
- Adopted `snake_case` variable naming

---

## Version 0.1.0

### Added

- Welcome screen
- User profile
- Simple calculator