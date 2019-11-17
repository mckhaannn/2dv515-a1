
export const fetchUsers = async () => {
  const res = await window.fetch('/users')
  const json = await res.json()
  return json
}

export const fetchRecomendedMovies = async (user, method, amount) => {
  const res = await window.fetch(`/${user}/${method}/${amount}`)
  const json = await res.json()
  return json
}
