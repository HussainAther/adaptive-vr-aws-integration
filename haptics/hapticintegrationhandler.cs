// Haptics/HapticIntegrationHandler.cs
using UnityEngine;
using System.Collections;

public static class HapticIntegrationHandler
{
    // Method to send haptic feedback based on intensity
    // "intensity" parameter should be a value between 0 and 1
    public static void SendHapticFeedback(float intensity)
    {
        // Ensure intensity is within range
        intensity = Mathf.Clamp(intensity, 0f, 1f);

        // Here we simulate haptic feedback using a simple log output.
        // Replace with actual haptic device API calls (e.g., Unity XR API for VR controllers).
        Debug.Log($"Sending haptic feedback with intensity: {intensity}");

        // Example: Using Unity's XR haptic feedback system (e.g., for Oculus or HTC Vive)
#if UNITY_XR
        var device = UnityEngine.XR.InputDevices.GetDeviceAtXRNode(UnityEngine.XR.XRNode.LeftHand); // Example for Left hand
        if (device.TryGetHapticCapabilities(out var capabilities) && capabilities.supportsImpulse)
        {
            float duration = 0.1f; // Short duration for a single pulse
            device.SendHapticImpulse(0, intensity, duration);
        }
#endif
    }

    // Simulated feedback for context-based learning
    public static void ContextualHapticFeedback(float comprehensionLevel)
    {
        // Example of adapting haptic feedback based on comprehension level
        float intensity = comprehensionLevel < 0.5f ? 0.3f : 0.7f;
        SendHapticFeedback(intensity);
    }

    // Simulate haptic feedback based on difficulty or guidance needs
    public static IEnumerator GuidanceFeedbackRoutine(float initialIntensity, float targetIntensity, float duration)
    {
        float elapsed = 0f;
        while (elapsed < duration)
        {
            float currentIntensity = Mathf.Lerp(initialIntensity, targetIntensity, elapsed / duration);
            SendHapticFeedback(currentIntensity);
            elapsed += Time.deltaTime;
            yield return null;
        }
        SendHapticFeedback(targetIntensity);
    }
}

