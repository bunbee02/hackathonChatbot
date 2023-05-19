// import { createStackNavigator } from '@react-navigation/stack';
import React, {useEffect, useState} from 'react';
// import SecondPage from './src/componets/SecondPage';
import ThirdPage from './src/componets/ThirdPage';
import MarketPage from './src/componets/MarketPage';
import ForthPage from './src/componets/ForthPage';
import FirstPage from './src/componets/FirstPage';
import {View} from 'react-native'


const App = () => {

  const [showFirstPage, setShowFirstPage] = useState(true)

  useEffect(() => {
    setTimeout(() =>{
      setShowFirstPage(false);
    },4000);
  },[]);

  return (
    <View style={{flex: 1}}>
      {showFirstPage ? <FirstPage/> : <ThirdPage/> }
    </View>
  );
};

export default App;
