import React  from 'react';
import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Image, View } from 'react-native';

 function FirstPage() {

  return (
    <View style={styles.container}>
    <Image source={require ('../../assets/Frame.png')}
      // style={{width: 80}}
      />
   
      <StatusBar style="auto" />
    </View>
  );
}



const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#4A682C',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
export default FirstPage;
