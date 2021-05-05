.. toolsforexperiments manual documentation master file, created by
   sphinx-quickstart on Thu Dec 17 11:12:40 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to the ToolsForExperiments Manual!
==========================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:


Overview
--------

This manual describes usage of some tools that help with running and analyzing experiments in an experimental
physics lab.
The workflows described have been designed to work with the research in the quantum circuits groups at UIUC and
the Hatlab at Pitt.
The tools use QCoDeS as the underlying measurement library to acquire data from scientific instruments.

In addition to QCoDeS we use these packages in our experiments:

   - `instrumentserver` -- allows using instruments across processes and computers.
   - `plottr` -- live plotting and quick inspection and analysis of data.
   - `labcore` -- a collection tools that make setting up and analysing commong measurement and analysis tasks easier
     and/or faster.

In this manual we will mainly focus on how to measure using these tools together.
Details and API docs can be found in the documentation of the individual packages
(at least eventually -- this is a very young effort, and a lot of documentation is admittedly still missing).

Our tool keep evolving, and so does this manual.
Things that we know aren't yet supported/working are called out as such.


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
