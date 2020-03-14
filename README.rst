
supervisor-stdout
=================

A simple `supervisord <http://supervisord.org/>`_ event listener to relay
process output to supervisor's stdout.

This is useful in situations where the output will be collected and set to
external logging framework, such as Heroku.

Credit
------

This is a forked, modified version of the original `supervisor-stdout <https://github.com/coderanger/supervisor-stdout>`_.

Installation
------------

Just install via pip or add to your requirements.txt:

.. code-block::

   pip install supervisor-stdout


Usage
-----

An example supervisord.conf:

.. code-block:: ini

   [supervisord]
   nodaemon = true

   [program:foo]
   command = ...
   stdout_events_enabled = true
   stderr_events_enabled = true

   [eventlistener:stdout]
   command = supervisor_stdout
   environment = PYTHONUNBUFFERED=1
   buffer_size = 1024
   events = PROCESS_LOG
   result_handler = supervisor_stdout:event_handler
   stderr_logfile = NONE
   stdout_logfile = NONE
