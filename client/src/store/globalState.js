import React, { useState } from 'react'
import useGlobalHook from 'use-global-hook'
import { fetchUsers, fetchRecomendedMovies } from '../actions/action'

const initialState = {
  users: [],
  movies: []
}

export const actions = {
  setUsers: async (store, users) => {
    let allUsers = await fetchUsers()
    store.setState({ users: allUsers })
  },
  setInformation: async (store, user, method, amount) => {
    let recomendedMovies = await fetchRecomendedMovies(user, method, amount)
    store.setState({ movies: recomendedMovies })
  }
}

export const useGlobal = useGlobalHook(React, initialState, actions)

export const GlobalContext = React.createContext()

const Store = ({ children }) => {
  const [globalState, globalActions] = useState([])
  return (
    <GlobalContext.Provider value={[globalState, globalActions]}>
      {children}
    </GlobalContext.Provider>
  )
}

export default Store
