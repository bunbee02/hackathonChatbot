import React from 'react';
import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Image, View, Text, Button } from 'react-native';


const styles = StyleSheet.create({
    container: {
      flex: 1,
      alignItems: 'center',
      justifyContent: 'center',
    },

    farmerImage: {
      objectFit: 'contain',
      width: '45%',
    },

    logoImage: {
      objectFit: 'contain',
      width: '16%',
      // marginBottom: '5%'

    },

    mainText: {
        fontSize:'28px',
        fontWeight: 300,
        marginBottom: '3%',
      },

    innerText: {
        fontWeight:'bold',
        fontSize: '28px',
      },

    subText:{
        fontSize: '15px',
        fontWeight: 300,
        textAlign: 'center',
        paddingLeft: '15%',
        paddingRight: '15%'
    }, 

    buttton:{
      fontSize: '55px',
      color:'red',
      backgroundColor:'blue',
      margin: '40%'
  } 
  });






function SecondPage() {
  return (
    <View style={styles.container}>
        <Image style={styles.logoImage} source={require ('../../assets/Frame2.png')}/> 
        <Image style={styles.farmerImage} source={require ('../../assets/farmer.png')} />
        <Text style={styles.mainText}>
            Meet  
          <Text style={styles.innerText}> Murimi!</Text>
        </Text>
        <Text style={styles.subText}>Our Farming Assistant, ready and eager to support you on your agricultural journey.</Text>
        <Button   
          style={styles.buttton}
          title="Get Started"
          // backgroundColor = '#4A682C'
          color='#4A682C'
          onPress={() => console.log('Button clicked')}
        />
        <StatusBar style="auto" />
    </View>
  );
}




export default SecondPage;
