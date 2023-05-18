import React from 'react';
import { View, TouchableOpacity, Text, StyleSheet, Image } from 'react-native';
// import { Ionicons } from '@expo/vector-icons';

const TalkToMurimiButton = () => {
  return (
    <View style={styles.container}>
      <TouchableOpacity style={styles.button}>
        <Text style={styles.buttonText}>Talk to Murimi</Text>
        <Image source={require ('../../assets/Layer.png')}
      // style={{width: 80}}
      />
      </TouchableOpacity>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    // position: 'relative',
    // position: 'absolute',
    // width: 800,
    // height: 43,
    // // left: '50%',
    // // top: 737,
    // // transform: [{ translateX: -160 }],
    // display: 'flex',
    // flexDirection: 'column',
    // justifyContent: 'center',
    alignItems: 'center',
    // paddingVertical: 7.5,
    // paddingHorizontal: 86,
    // // gap: 10,
  },
  button: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: 'transparent',
    borderWidth: 0.5,
    borderRadius: 10,
    width: 326,
    height: 43,
    justifyContent: 'center',
    marginTop: 8
  },
  buttonText: {
    color: '#4A682C',
    fontSize: 16,
    marginRight: 25,
  },
});

export default TalkToMurimiButton;