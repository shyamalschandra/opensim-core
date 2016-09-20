"""
Test DataTable interface.
"""
import os, unittest
import opensim as osim

class TestDataTable(unittest.TestCase):
    def test_DataTable(self):
        table = osim.DataTable()
        # Set column labels.
        table.setColumnLabels(['0', '1', '2', '3'])
        assert table.getColumnLabels() == ('0', '1', '2', '3')
        assert table.hasColumn('0')
        assert table.hasColumn('2')
        table.setColumnLabel(0, 'zero')
        table.setColumnLabel(2, 'two')
        assert table.getColumnLabel(0) == 'zero'
        assert table.getColumnLabel(2) == 'two'
        assert table.getColumnIndex('zero') == 0
        assert table.getColumnIndex('two')  == 2
        # Append a row to the table.
        row = osim.RowVector([1, 2, 3, 4])
        table.appendRow(0.1, row)
        assert table.getNumRows() == 1
        assert table.getNumColumns() == 4
        row0 = table.getRowAtIndex(0)
        assert (row0[0] == row[0] and
                row0[1] == row[1] and
                row0[2] == row[2] and
                row0[3] == row[3])
        # Append another row to the table.
        row[0] *= 2
        row[1] *= 2
        row[2] *= 2
        row[3] *= 2
        table.appendRow(0.2, row)
        assert table.getNumRows() == 2
        assert table.getNumColumns() == 4
        row1 = table.getRow(0.2)
        assert (row1[0] == row[0] and
                row1[1] == row[1] and
                row1[2] == row[2] and
                row1[3] == row[3])
        # Append another row to the table.
        row[0] *= 2
        row[1] *= 2
        row[2] *= 2
        row[3] *= 2
        table.appendRow(0.3, row)
        assert table.getNumRows() == 3
        assert table.getNumColumns() == 4
        row2 = table.getRow(0.3)
        assert (row2[0] == row[0] and
                row2[1] == row[1] and
                row2[2] == row[2] and
                row2[3] == row[3])
        # Retrieve independent column.
        assert table.getIndependentColumn() == (0.1, 0.2, 0.3)
        # Retrieve dependent columns.
        col1 = table.getDependentColumnAtIndex(1)
        assert (col1[0] == 2 and
                col1[1] == 4 and
                col1[2] == 8)
        col3 = table.getDependentColumn('3')
        assert (col3[0] == 4 and
                col3[1] == 8 and
                col3[2] == 16)
        assert table.hasColumn(0)
        assert table.hasColumn(2)

        table = osim.DataTable()
        table.setColumnLabels(['col0', 'col1', 'col2', 'col3'])
        row = osim.RowVector([1, 1, 1, 1])
        table.appendRow(0.1, row)
        row = osim.RowVector([2, 2, 2, 2])
        table.appendRow(0.2, row)
        row = osim.RowVector([3, 3, 3, 3])
        table.appendRow(0.3, row)
        print table.getRowAtIndex(0)[3]
        print table.getRowAtIndex(0)[4]


    def test_TimeSeriesTable(self):
        table = osim.TimeSeriesTable()
        table.setColumnLabels(('col1', 'col2', 'col3', 'col4'))
        assert(table.getColumnLabels() == ('col1', 'col2', 'col3', 'col4'))
        # Append a row to the table.
        row = osim.RowVector([1, 2, 3, 4])
        table.appendRow(0.1, row)
        assert table.getNumRows() == 1
        assert table.getNumColumns() == 4
        row0 = table.getRowAtIndex(0)
        assert (row0[0] == row[0] and
                row0[1] == row[1] and
                row0[2] == row[2] and
                row0[3] == row[3])
        # Append another row to the table.
        row[0] *= 2
        row[1] *= 2
        row[2] *= 2
        row[3] *= 2
        table.appendRow(0.2, row)
        assert table.getNumRows() == 2
        assert table.getNumColumns() == 4
        row1 = table.getRow(0.2)
        assert (row1[0] == row[0] and
                row1[1] == row[1] and
                row1[2] == row[2] and
                row1[3] == row[3])
        # Append another row to the table with a timestamp
        # less than the previous one. Exception expected.
        try:
            table.appendRow(0.15, row)
            assert False
        except RuntimeError:
            pass

    def test_DataTableVec3(self):
        table = osim.DataTableVec3()
        # Set columns labels.
        table.setColumnLabels(['0', '1', '2'])
        assert table.getColumnLabels() == ('0', '1', '2')
        # Append a row to the table.
        row = osim.RowVectorOfVec3([osim.Vec3(1, 2, 3), 
                                    osim.Vec3(4, 5, 6),
                                    osim.Vec3(7, 8, 9)])
        table.appendRow(0.1, row)
        assert table.getNumRows() == 1
        assert table.getNumColumns() == 3
        row0 = table.getRowAtIndex(0)
        assert (str(row0[0]) == str(row[0]) and
                str(row0[1]) == str(row[1]) and
                str(row0[2]) == str(row[2]))
        # Append another row to the table.
        row = osim.RowVectorOfVec3([osim.Vec3( 2,  4,  6), 
                                    osim.Vec3( 8, 10, 12),
                                    osim.Vec3(14, 16, 18)])
        table.appendRow(0.2, row)
        assert table.getNumRows() == 2
        assert table.getNumColumns() == 3
        row1 = table.getRow(0.2)
        assert (str(row1[0]) == str(row[0]) and
                str(row1[1]) == str(row[1]) and
                str(row1[2]) == str(row[2]))
        # Append another row to the table.
        row = osim.RowVectorOfVec3([osim.Vec3( 4,  8, 12), 
                                    osim.Vec3(16, 20, 24),
                                    osim.Vec3(28, 32, 36)])
        table.appendRow(0.3, row)
        assert table.getNumRows() == 3
        assert table.getNumColumns() == 3
        row2 = table.getRow(0.3)
        assert (str(row2[0]) == str(row[0]) and
                str(row2[1]) == str(row[1]) and
                str(row2[2]) == str(row[2]))
        # Retrieve independent column.
        assert table.getIndependentColumn() == (0.1, 0.2, 0.3)
        # Retrieve dependent columns.
        col1 = table.getDependentColumnAtIndex(1)
        assert (str(col1[0]) == str(osim.Vec3( 4,  5,  6)) and
                str(col1[1]) == str(osim.Vec3( 8, 10, 12)) and
                str(col1[2]) == str(osim.Vec3(16, 20, 24)))
        col2 = table.getDependentColumn('2')
        assert (str(col2[0]) == str(osim.Vec3( 7,  8,  9)) and
                str(col2[1]) == str(osim.Vec3(14, 16, 18)) and
                str(col2[2]) == str(osim.Vec3(28, 32, 36)))

    def test_TimeSeriesTableVec3(self):
        table = osim.TimeSeriesTableVec3()
        # Set columns labels.
        table.setColumnLabels(['0', '1', '2'])
        assert table.getColumnLabels() == ('0', '1', '2')
        # Append a row to the table.
        row = osim.RowVectorOfVec3([osim.Vec3(1, 2, 3), 
                                    osim.Vec3(4, 5, 6),
                                    osim.Vec3(7, 8, 9)])
        table.appendRow(0.1, row)
        assert table.getNumRows() == 1
        assert table.getNumColumns() == 3
        row0 = table.getRowAtIndex(0)
        assert (str(row0[0]) == str(row[0]) and
                str(row0[1]) == str(row[1]) and
                str(row0[2]) == str(row[2]))
        # Append another row to the table.
        row = osim.RowVectorOfVec3([osim.Vec3( 2,  4,  6), 
                                    osim.Vec3( 8, 10, 12),
                                    osim.Vec3(14, 16, 18)])
        table.appendRow(0.2, row)
        assert table.getNumRows() == 2
        assert table.getNumColumns() == 3
        row1 = table.getRow(0.2)
        assert (str(row1[0]) == str(row[0]) and
                str(row1[1]) == str(row[1]) and
                str(row1[2]) == str(row[2]))
        # Append another row to the table with a timestamp
        # less than the previous one. Exception expected.
        try:
            table.appendRow(0.15, row)
            assert False
        except RuntimeError:
            pass
