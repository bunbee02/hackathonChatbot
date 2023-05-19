import React from "react";
import { View, Text, TouchableOpacity, Image, StyleSheet, Modal, Button } from "react-native";
import {marketData} from './Data';
import HomeIcons from "./HomeIcons";


const ThirdPage = () => {

  const handleImageClick = (text) => {
    ;
  };


  return (
    <View>
    <Text style={styles.mainHeading}>Our Market Place</Text>
    <View style={styles.container}>
      {marketData.map((item, index) => (
        <TouchableOpacity
          key={index}
          style={styles.imageContainer}
          onPress={() => handleImageClick(item.text)}
        >
          <Image source={item.image} />
          <Text style={styles.marketHeading}>Tap to View</Text>
        </TouchableOpacity>
      ))}
      <HomeIcons/>

      <View style={styles.greenBorder} /> 

    </View>
    </View>

  );
};


const styles = StyleSheet.create({
  container: {
    flex: 1,
    flexDirection: "row",
    flexWrap: "wrap",
    justifyContent: "space-between",
    position: 'relative'
  },

  imageContainer: {
    width: "50%",
    aspectRatio: 1,
    justifyContent: "center",
    alignItems: "center",
  
  },

  image: {
    resizeMode: "cover",
  },

  mainHeading: {
    color: 'black',
    paddingTop: 40,
    paddingLeft: 30,
    fontSize: 16,
    color: '#4A682C'
  },
  marketHeading:{
    color:'#4A682C',
    paddingTop: 10,
    fontWeight: 400
  }


});

export default ThirdPage;