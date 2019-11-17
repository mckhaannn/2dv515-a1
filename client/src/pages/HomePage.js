import React, { useEffect, useState } from 'react'
import { useGlobal } from '../store/globalState'
import Result from './Result'

import InputLabel from '@material-ui/core/InputLabel'
import MenuItem from '@material-ui/core/MenuItem'
import FormControl from '@material-ui/core/FormControl'
import Select from '@material-ui/core/Select'
import { makeStyles, useTheme } from '@material-ui/core/styles'
import Input from '@material-ui/core/Input'
import TextField from '@material-ui/core/TextField'
import Button from '@material-ui/core/Button'
import Icon from '@material-ui/core/Icon'

const useStyles = makeStyles(theme => ({
  formControl: {
    margin: theme.spacing(1),
    minWidth: 120,
    maxWidth: 300
  },
  chips: {
    display: 'flex',
    flexWrap: 'wrap'
  },
  chip: {
    margin: 2
  },
  noLabel: {
    marginTop: theme.spacing(3)
  },
  container: {
    display: 'flex',
    flexWrap: 'wrap'
  },
  textField: {
    marginLeft: theme.spacing(1),
    marginRight: theme.spacing(1),
    width: 200
  },
  button: {
    margin: theme.spacing(1)
  },
  input: {
    display: 'none'
  }
}))

const ITEM_HEIGHT = 48
const ITEM_PADDING_TOP = 8
const MenuProps = {
  PaperProps: {
    style: {
      maxHeight: ITEM_HEIGHT * 4.5 + ITEM_PADDING_TOP,
      width: 250
    }
  }
}

const methods = [
  'Euclidean',
  'Pearson'
]

function getStyles (name, theme) {
  return {
    fontWeight:
        theme.typography.fontWeightMedium
  }
}

export default function MultipleSelect () {
  const classes = useStyles()
  const theme = useTheme()
  const [globalState, globalActions] = useGlobal()
  const [showList, setShowList] = useState(false)
  const [values, setValues] = useState({
    user: '',
    method: '',
    amount: ''
  })

  const handleChange = prop => event => {
    setValues({ ...values, [prop]: event.target.value })
  }
  const handleMenuItemClick = () => {
    if (values.user !== '' && values.method !== '' && values.amount !== '') {
      globalActions.setInformation(values.user, values.method, values.amount)

      setShowList(true)
    }
  }

  useEffect(() => {
    getUsers()
  }, [])

  async function getUsers () {
    globalActions.setUsers()
  }

  return (
    <div>
      <FormControl className={classes.formControl}>
        <InputLabel id='demo-mutiple-name-label'>User</InputLabel>
        <Select
          labelId='demo-mutiple-name-label'
          id='demo-mutiple-name'
          value={values.user}
          onChange={handleChange('user')}
          input={<Input />}
          MenuProps={MenuProps}
        >
          {globalState.users.map(x => (
            <MenuItem key={x.userId} value={x.name}> {x.name}</MenuItem>
          ))}
        </Select>
      </FormControl>
      <FormControl className={classes.formControl}>
        <InputLabel id='demo-mutiple-name-label'>Method</InputLabel>
        <Select
          labelId='demo-mutiple-name-label'
          id='demo-mutiple-name'
          value={values.method}
          onChange={handleChange('method')}
          input={<Input />}
          MenuProps={MenuProps}
        >
          {methods.map(methods => (
            <MenuItem key={methods} value={methods} style={getStyles(methods, theme)}>
              {methods}
            </MenuItem>
          ))}
        </Select>
        <form className={classes.container} noValidate autoComplete='off'>
          <div>
            <TextField
              id='standard-basic'
              value={values.amount}
              onChange={handleChange('amount')}
              className={classes.textField}
              label='Results'
              margin='normal'
            />
          </div>
        </form>
        <Button
          variant='contained'
          color='primary'
          className={classes.button}
          endIcon={<Icon>send</Icon>}
          onClick={event => handleMenuItemClick()}
        >
        Send
        </Button>
      </FormControl>
      {showList ? <Result /> : null}
    </div>
  )
}
