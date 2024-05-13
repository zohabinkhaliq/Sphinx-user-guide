Troubleshooting
===============

Here are the few possible issues you might encounter 

- Python installation 
   You might encounter this issue because, Python might be installed twice. 
   Go to the directory were python was installed, and delete all the files. Once done install python again. 
- Sphinx project not created 
   If you created a sphinx project, and you not able to view the folder in explorer. This happens due to the format of the file name. 
   Make sure the name of the file is in small letters and all caps.
- To swicth between themes
   At times, you might not be able to switch between themes. This happens if relevant changes are not made in confi.py file and if theme is not installed using pip. 
   For instance; here is an example to switch to sphinx-rtd-theme
   
   - Step 1: Run the following command on command prompt ``pip install sphinx-rtd-theme``
   - Step 2: Go to confi.py file located in source folder and add the following 

   .. code-block:: 

            import sphinx_rtd_theme

            #Add 'sphinx_rtd_theme' to the extensions list
            extensions = []
            templates_path=['sphinx_rtd_theme',]
            exclude_patterns = []




