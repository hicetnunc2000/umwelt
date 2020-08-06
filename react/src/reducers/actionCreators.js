const AUTH = 'AUTH'
const FORM = 'FORM'

export const auth = () => {
    return {
        type: AUTH
    }
}

export const formUpdate = (obj) => {
    return {
        type: FORM,
        obj: obj
    }
}