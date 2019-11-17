import React, { useEffect, useState } from 'react'
import { useGlobal } from '../store/globalState'
import { makeStyles } from '@material-ui/core/styles'
import Table from '@material-ui/core/Table'
import TableBody from '@material-ui/core/TableBody'
import TableCell from '@material-ui/core/TableCell'
import TableHead from '@material-ui/core/TableHead'
import TableRow from '@material-ui/core/TableRow'
import Paper from '@material-ui/core/Paper'

const useStyles = makeStyles({
  root: {
    width: '100%',
    overflowX: 'auto'
  },
  table: {
    minWidth: 650
  }
})

export default function SimpleTable () {
  const classes = useStyles()

  const [globalState, globalActions] = useGlobal()

  const asd = () => {
    return globalState.movies.map(x => {
      return (<TableRow key={x.movie}>
        <TableCell component='th' scope='row'>
          {x.movie}
        </TableCell>
        <TableCell align='right'>{x.weighted_score}</TableCell>
      </TableRow>
      )
    })
  }

  return (
    <Paper className={classes.root}>
      <Table className={classes.table} aria-label='simple table'>
        <TableHead>
          <TableRow>
            <TableCell>Movie</TableCell>
            <TableCell align='right'>Score</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {asd()}
        </TableBody>
      </Table>
    </Paper>
  )
}
