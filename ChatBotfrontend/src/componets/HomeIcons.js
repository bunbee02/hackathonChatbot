import React from "react";
import { View, Text, TouchableOpacity, Image, StyleSheet, Modal, Button } from "react-native";


const HomeIcons = () => {
  return(
    <View style={styles.iconsContainer} >
    <TouchableOpacity style={styles.iconContainer} >
    <Image source={require('../../assets/home.png')}/>
    <Text>Home</Text>
    </TouchableOpacity>
    <TouchableOpacity style={styles.iconContainer}>
    <Image source={require('../../assets/market.png')}/>
    <Text style={styles.iconText}>Market</Text>
    </TouchableOpacity>
    <TouchableOpacity style={styles.iconContainer}>
    <Image source={require('../../assets/settings.png')}/>
    <Text style={styles.iconText}>Settings</Text>
    </TouchableOpacity>
    </View>
    )
};

const styles = StyleSheet.create({
iconsContainer:{
    flexDirection: "row",
    justifyContent: "center",
    alignItems: "center",
    paddingVertical: 28 ,
    paddingLeft : 18,
    marginLeft: 1,
  },

  iconContainer: {
    display : "flex",
    justifyContent: 'base',
    alignItems: "center",
    flexWrap : "nowrap",
    width: 100,
  },

})

export default HomeIcons;