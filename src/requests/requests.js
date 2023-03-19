import axios from "axios"

const BASE_URL = "http://127.0.0.1:8000"

export async function getNRELDataRequest(formData) {
    const config = {
        headers: {

        }
    }

    const response = await axios.post(
        `${BASE_URL}/api/nrel/`,
        formData,
        config
    )
    return response
}
