## 🔬 Laser Beam Spot Size Measurement using Image Processing

### Overview
This project presents an image-processing–based system to measure the **laser beam spot size and intensity profile** using captured CCD camera images. The work demonstrates how computer vision techniques can be applied to **physical measurement and experimental diagnostics**.

The project was developed as part of an academic research effort and reflects a **research-oriented Proof-of-Concept (PoC)** approach.

---

### Problem Statement
Accurate measurement of laser beam profiles is essential in optics and experimental physics. Traditional measurement techniques require specialized hardware. This project explores a **software-driven alternative**, leveraging image processing to extract beam characteristics from digital images.

---

### Methodology
1. Image acquisition using a CCD camera
2. Preprocessing (grayscale conversion, noise reduction)
3. Thresholding and beam isolation
4. Intensity distribution analysis
5. Estimation of beam spot size and profile

---

### Technologies Used
- Python  
- OpenCV  
- NumPy  
- SciPy  
- Matplotlib  

---

### Results
- Successful extraction of laser beam region from background  
- Computation of beam spot size based on intensity distribution  
- Visualization of beam profile and measurement results  

---

### Applications
- Optical system diagnostics  
- Experimental physics and photonics  
- Image-based measurement systems  
- Computer vision R&D applications  

---

### Future Improvements
- Sub-pixel precision measurement  
- Noise-robust beam fitting techniques  
- Synthetic beam profile generation for testing  
- Integration with real-time acquisition systems  

---

### Disclaimer
This project is intended for academic and research demonstration purposes only. No sensitive or proprietary data is included.


## Support
Tell people where they can go to for help. It can be any combination of an issue tracker, a chat room, an email address, etc.

## Roadmap
If you have ideas for releases in the future, it is a good idea to list them in the README.

## Contributing
State if you are open to contributions and what your requirements are for accepting them.

For people who want to make changes to your project, it's helpful to have some documentation on how to get started. Perhaps there is a script that they should run or some environment variables that they need to set. Make these steps explicit. These instructions could also be useful to your future self.

You can also document commands to lint the code or run tests. These steps help to ensure high code quality and reduce the likelihood that the changes inadvertently break something. Having instructions for running tests is especially helpful if it requires external setup, such as starting a Selenium server for testing in a browser.

## Authors and acknowledgment
Show your appreciation to those who have contributed to the project.

## License
For open source projects, say how it is licensed.

## Project status
If you have run out of energy or time for your project, put a note at the top of the README saying that development has slowed down or stopped completely. Someone may choose to fork your project or volunteer to step in as a maintainer or owner, allowing your project to keep going. You can also make an explicit request for maintainers.
