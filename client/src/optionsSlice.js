import { createSlice } from '@reduxjs/toolkit';

const initialState = {
  options: ["score", "conditionals"]
}

const optionsSlice = createSlice({
  name: "options",
  initialState,
  reducers: {
    change: (state, action) => {
      state.options = action.payload;
    }
  }
})

export const {change} = optionsSlice.actions;
export default optionsSlice.reducer;