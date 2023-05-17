import React from 'react';
import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Image, View, Text } from 'react-native';


const styles = StyleSheet.create({
    container: {
        margin: 0
    //   flex: 1,
    //   alignItems: 'center',
    //   justifyContent: 'center',
    },

    mainText: {
        fontSize:'30px'
      },

    innerText: {
        fontWeight: 500,
      },
    subText:{
        fontSize: '16px',
        fontWeight: 300,
        color: 'red'
    }  
  });






function SecondPage() {
  return (
    <View style={styles.container}>
    <Image source={require ('logo.svg')} />
    <Image source={require ('Frame2.png')}/>  
    <Text>
        Meet 
      <Text style={styles.innerText}>Murimi!</Text>
    </Text>
    <Text>Our Farming Assistant, ready and eager to support you on your agricultural journey.</Text>
    <StatusBar style="auto" />
    </View>
  );
}




export default SecondPage;
