export const COLUMNS = [
  {
    Header: 'Code',
    Footer: 'Code',
    accessor: 'code'
  },
  {
    Header: 'Score',
    Footer: 'Score',
    accessor: 'score'
  },
  {
    Header: 'Conditionals',
    Footer: 'Conditionals',
    accessor:'conditionals'
  },
  {
    Header: 'Loops',
    Footer: 'Loops',
    accessor:'loops'
  },
  {
    Header: 'Functions',
    Footer: 'Functions',
    accessor:'functions'
  },
  {
    Header: 'Functions recursion',
    Footer: 'Functions recursion',
    accessor:'functions_recursion'
  },
  {
    Header: 'Max depth',
    Footer: 'Max depth',
    accessor:'max_depth'
  },
  {
    Header: 'Average depth',
    Footer: 'Average depth',
    accessor:'avg_depth'
  },
  {
    Header: 'Sum depth',
    Footer: 'Sum depth',
    accessor:'sum_depth'
  }
]

export const GROUPED_COLUMNS = [
  {
    Header: 'Code',
    Footer: 'Code',
    accessor: 'code'
  },
  {
    Header: 'Conditionals',
    Footer: 'Conditionals',
    columns:[
        {
    Header: 'Conditionals',
    Footer: 'Conditionals',
    accessor:'conditionals'
  },
    ]
  },
  {
    Header: 'Loop',
    Footer: 'Loop',
    columns: [
      {
        Header: 'Loops',
        Footer: 'Loops',
        accessor:'loops'
      },
      {
        Header: 'Loops for',
        Footer: 'Loops for',
        accessor:'loops_for'
      },
      {
        Header: 'Loops while',
        Footer: 'Loops while',
        accessor:'loops_while'
      },
    ]
  },
  {
    Header: 'Function',
    Footer: 'Function',
    columns:[
      {
        Header: 'Functions',
        Footer: 'Functions',
        accessor:'functions'
      },
      {
        Header: 'Functions recursion',
        Footer: 'Functions recursion',
        accessor:'functions_recursion'
      },
    ]
  },
  {
    Header: 'Depth',
    Footer: 'Depth',
    columns:[
      {
        Header: 'Max depth',
        Footer: 'Max depth',
        accessor:'max_depth'
      },
      {
        Header: 'Average depth',
        Footer: 'Average depth',
        accessor:'avg_depth'
      },
      {
        Header: 'Sum depth',
        Footer: 'Sum depth',
        accessor:'sum_depth'
      }
    ]
  }
]