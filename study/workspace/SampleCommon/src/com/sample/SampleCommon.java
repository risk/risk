package com.sample;

public class SampleCommon {
	public static String createMessage(Object o) {
		return "my class name is " + o.getClass().getSimpleName();
	}
}
