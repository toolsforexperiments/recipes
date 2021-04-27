import os

from instrumentserver import QtWidgets
from instrumentserver.client import Client as InstrumentClient
from instrumentserver.gui import widgetDialog
from instrumentserver.gui.instruments import ParameterManagerGui


def main():
    # create a Qt application
    app = QtWidgets.QApplication([])

    # open a client to a server using default address (localhost) and port.
    cli = InstrumentClient()

    # on the server side, create an instance of a parameter manager virtual instrument if it doesn't exist yet.
    # if it does, just get the existing one.
    if 'params' in cli.list_instruments():
        param_mgr = cli.get_instrument('params')
    else:
        param_mgr = cli.create_instrument(
            'instrumentserver.params.ParameterManager',
            'params'
        )
        if os.path.exists("parameters.json"):
            param_mgr.fromFile("parameters.json")

    # create the GUI for the parameter manager
    _ = widgetDialog(ParameterManagerGui(param_mgr))

    # important to actually run the GUI
    return app.exec_()


if __name__ == '__main__':
    main()

