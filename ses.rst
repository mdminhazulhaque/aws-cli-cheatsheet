SES
===

Send Mail
---------

.. code:: bash

   aws ses send-email \
    --to user@example.com \
    --subject Howdy \
    --html '<h1>Hello, Mate!</h1>' \
    --from noreply@example.com