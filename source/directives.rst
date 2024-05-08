Sphinx directives
===============

In this section few helpful sphinx directives are listed. 

Headings (Different levels)
+++++++++++++++++++++++++++

.. code::

    Heading 1
    =========

    Heading 2
    ++++++++

    Heading 3
    ---------

    Heading 4
    *********

    Heading 5
    ^^^^^^^^^

    Heading 6
    ########

    Heading 7
    ~~~~~~~~


.. note::
   The number of symbols below the headings should be equal to the length of the line. 
.. end-note::

Writing styles
++++++++++++++

Following are the syntaxes for different styles:

- Bold: Use this for bold ``**Content to be bold**``
- Italics: Use this for italicizing ``*Content to be italicized*``
- Superscript: Use this for subscripting ``:sup:`Text as subscript'``

Tables 
++++++

Following are the few syntax to add different type of tables 

List Tables: (Example)

.. list-table:: Frozen Delights!
   :widths: 25 25 50
   :header-rows: 1
    
   * - Treat
     - Quantity
     - Description
   * - Albatross
     - 2.99
     - On a stick!
   * - Crunchy Frog
     - 1.49
     - If we took the bones out, it wouldn't be crunchy, now would it?
   * - Gannet Ripple
     - 1.99
     - On a stick!

.. list-table:: Title
   :widths: 25 25 50
   :header-rows: 1

   * - Heading row 1, column 1
     - Heading row 1, column 2
     - Heading row 1, column 3
   * - Row 1, column 1
     -
     - Row 1, column 3
   * - Row 2, column 1
     - Row 2, column 2
     - Row 2, column 3


COMPLEX TABLE:

+------------+------------+-----------+
| Header 1   | Header 2   | Header 3  |
+============+============+===========+
| body row 1 | column 2   | column 3  |
+------------+------------+-----------+
| body row 2 | Cells may span columns.|
+------------+------------+-----------+
| body row 3 | Cells may  | - Cells   |
+------------+ span rows. | - contain |
| body row 4 |            | - blocks. |
+------------+------------+-----------+

SIMPLE TABLE:

=====  =====  ======
   Inputs     Output
------------  ------
  A      B    A or B
=====  =====  ======
False  False  False
True   False  True
False  True   True
True   True   True
=====  =====  ======



