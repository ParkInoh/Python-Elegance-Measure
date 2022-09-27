import React, { useMemo } from 'react';
import { useLocation } from 'react-router';
import { COLUMNS, GROUPED_COLUMNS } from '../../column';
import { useSortBy, useTable } from 'react-table';
import './table.css'
const Table = () => {
  const location = useLocation().state.data;
  const elegantData = JSON.parse(location.data);
  const fileList = Object.keys(elegantData);
  let chartList = [];
  for(let i = 0; i < fileList.length; i++){
    let tmp = elegantData[fileList[i]];
    tmp['code'] = fileList[i];
    chartList.push(tmp);
  }
  const columns = useMemo(() => COLUMNS, []);
  const data = useMemo(() => chartList, []);
  const tableInstance = useTable({
    columns,
    data,
  }, useSortBy)

  const {
    getTableProps,
    getTableBodyProps,
    headerGroups,
    footerGroups,
    rows,
    prepareRow
  } = tableInstance;
  return(
    <table {...getTableProps()}>
      <thead>
        {headerGroups.map(headerGroup => (
            <tr {...headerGroup.getHeaderGroupProps()}>
              {headerGroup.headers.map(column => (
                  <th {...column.getHeaderProps(column.getSortByToggleProps())}>
                    {column.render('Header')}
                    <span>
                      {column.isSorted ? (column.isSortedDesc ? '🔽' : '🔼') : ''}
                    </span>
                  </th>
                ))}
            </tr>
          ))}
      </thead>
      <tbody {...getTableBodyProps()}>
        {rows.map(row => {
            prepareRow(row)
            return (
              <tr {...row.getRowProps()}>
                {row.cells.map(cell => (
                    <td {...cell.getCellProps()}>{cell.render('Cell')}</td>
                ))}
              </tr>
            )
          })}
      </tbody>
      <tfoot>
        {
          footerGroups.map(footerGroup => (
            <tr {...footerGroup.getFooterGroupProps()}>
              {footerGroup.headers.map(column => (
                  <td {...column.getFooterProps}>
                    {column.render('Footer')}
                  </td>
                ))}
            </tr>
          ))
        }
      </tfoot>
    </table>
  )
};

export default Table;