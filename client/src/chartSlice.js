import { createSlice } from '@reduxjs/toolkit';

const initialState = {
  chartData: {}
}

const chartSlice = createSlice({
  name: "chartData",
  initialState,
  reducers: {
    change: (state, action) => {
      state.chart = action.payload;
    }
  }
})

export const {change} = chartSlice.actions;
export default chartSlice.reducer;