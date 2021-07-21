# ar-debug-workbench
Augmented reality workbench for printed circuit board (PCB) debugging.

/ardw-plugin/ has the code for the KiCAD action plugin. To enable it, place the folder in the appropriate /scripting/plugins/ directory (see [IBOM's installation instructions](https://github.com/openscopeproject/InteractiveHtmlBom/wiki/Installation) for details). To use it, open a project in EESchema and File>Plot all pages as svg into the folder ./ardw/ (must create the first time). Then, open the project in pcbnew and click the icon on the toolbar. Two json files will show up in the /ardw/ folder and the svgs will be updated. Copying these files to /ardw-app/data/ will allow the app to run with them.

/ardw-app/ has the code for the web application. To use, run 'npm start' from the directory, then go to localhost:3000.

WARNING: this is no longer the most current version (see branch python-server)
